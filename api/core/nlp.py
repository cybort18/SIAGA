from transformers import pipeline

# --- MUAT SEMUA MODEL SEKALI SAAT SERVER DIMULAI ---
print("Memuat pipeline NER...")
# Menggunakan model NER yang sudah terlatih untuk Bahasa Indonesia
ner_pipeline = pipeline(
    "ner",
    model="cahya/bert-base-indonesian-ner",
    grouped_entities=True  # Sangat penting untuk menggabungkan token seperti 'Grand', '##Indonesia'
)
print("Pipeline NER dimuat.")


print("Memuat pipeline Klasifikasi...")
# Model klasifikasi yang sudah Anda rencanakan (pilihan bagus!)
clf_pipeline = pipeline(
    "text-classification",
    model="../api/models/classification_model" # Pastikan path ini benar dari lokasi Anda melatih model
)
print("Pipeline Klasifikasi dimuat.")


# --- FUNGSI-FUNGSI LOGIKA ---

def extract_entities(text: str) -> list:
    """Mengekstrak entitas dari teks menggunakan pipeline Hugging Face."""
    ner_results = ner_pipeline(text)
    
    # Format ulang hasil agar sesuai dengan struktur API kita
    # Anda bisa menambahkan pemetaan label di sini jika perlu
    # Contoh: 'B-LOC' -> 'LOKASI'
    label_map = {
        'B-LOC': 'LOKASI',
        'I-LOC': 'LOKASI',
        'B-OBJ': 'OBJEK',
        'I-OBJ': 'OBJEK',
        'B-PER': 'ORANG', # Person
        'I-PER': 'ORANG',
        # Tambahkan pemetaan lain jika ada
    }

    formatted_entities = []
    for entity in ner_results:
        # Gunakan label dari map, atau label asli jika tidak ada di map
        mapped_label = label_map.get(entity['entity_group'], entity['entity_group'])
        
        formatted_entities.append({
            "text": entity['word'],
            "label": mapped_label
        })
        
    return formatted_entities


def classify_text(text: str) -> dict:
    """Mengklasifikasikan teks menggunakan pipeline Hugging Face."""
    result = clf_pipeline(text)[0]  # Hasilnya adalah list, ambil elemen pertama
    return {"category": result['label'], "confidence": result['score']}