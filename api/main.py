# api/main.py
import uvicorn
import shutil
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

# Import fungsi-fungsi kita
from core.stt import transcribe_audio
from core.nlp import extract_entities, classify_text

app = FastAPI(
    title="SIAGA 112 AI Engine",
    description="API untuk triase panggilan darurat menggunakan AI."
)

# Definisikan struktur data untuk response (baik untuk dokumentasi otomatis)
class Entity(BaseModel):
    text: str
    label: str

class TriageResult(BaseModel):
    transcription: str
    category: str
    confidence: float
    entities: List[Entity]

@app.post("/triage", response_model=TriageResult)
async def process_emergency_call(audio_file: UploadFile = File(...)):
    """
    Endpoint utama untuk memproses panggilan darurat dari file audio.
    1. Terima file audio.
    2. Transkripsi audio menjadi teks.
    3. Klasifikasikan teks untuk menentukan kategori darurat.
    4. Ekstrak entitas (lokasi, insiden) dari teks.
    5. Kembalikan hasil terstruktur.
    """
    # Buat direktori temporary jika belum ada
    temp_dir = "temp_audio"
    os.makedirs(temp_dir, exist_ok=True)
    
    temp_file_path = os.path.join(temp_dir, audio_file.filename)

    # Simpan file audio yang di-upload secara temporer
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(audio_file.file, buffer)

        # 1. Speech-to-Text
        transcribed_text = transcribe_audio(temp_file_path)
        if not transcribed_text:
            raise HTTPException(status_code=400, detail="Gagal mentranskripsi audio atau audio kosong.")

        # 2. Klasifikasi
        classification_result = classify_text(transcribed_text)
        
        # 3. NER
        entities_result = extract_entities(transcribed_text)

        # 4. Format dan kirim response
        return TriageResult(
            transcription=transcribed_text,
            category=classification_result['category'],
            confidence=classification_result['confidence'],
            entities=entities_result
        )

    except Exception as e:
        # Menangkap error umum dan memberikan response yang lebih baik
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Selalu hapus file temporary setelah selesai
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

@app.get("/")
def read_root():
    return {"status": "SIAGA 112 AI Engine is running"}

# Untuk menjalankan server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)