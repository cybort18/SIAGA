from google.cloud import speech
import os
from pathlib import Path

# Membangun path ke file kredensial secara dinamis dan andal.
credential_path = Path(__file__).resolve().parents[2] / 'gcp-credentials.json'

def transcribe_audio(audio_file_path: str) -> str:
    """
    Mengonversi file audio ke teks menggunakan Google Cloud Speech-to-Text.
    """
    try:
        # Inisialisasi client dengan menunjuk langsung ke file kredensial.
        client = speech.SpeechClient.from_service_account_file(credential_path)
    except Exception as e:
        # Ini adalah error fatal jika file kredensial tidak ditemukan.
        print(f"FATAL ERROR: Gagal memuat service account file. Cek path. Error: {e}")
        return ""

    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="id-ID",
        enable_automatic_punctuation=True
    )

    try:
        response = client.recognize(config=config, audio=audio)
        if response.results:
            return response.results[0].alternatives[0].transcript
        else:
            # Tidak ada hasil, kembalikan string kosong (bukan error).
            return ""
    except Exception as e:
        # Biarkan baris ini. Ini berguna jika Google API memberikan error.
        print(f"Error during transcription from Google API: {e}")
        return ""