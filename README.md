# SIAGA 112 - AI Engine 🚀

Mesin AI untuk proyek **AI Innovation Challenge COMPFEST 17**. Proyek ini bertujuan untuk meningkatkan efisiensi dan kecepatan respons layanan panggilan darurat di Jakarta melalui sistem triase cerdas berbasis AI.

## 📄 Deskripsi Proyek

SIAGA 112 berfungsi sebagai lapisan respons pertama untuk panggilan darurat. Sistem ini menggunakan teknologi Artificial Intelligence untuk secara otomatis mentranskripsi, mengklasifikasikan, dan mengekstrak informasi penting dari panggilan suara, membebaskan operator manusia untuk fokus pada kasus-kasus yang paling kritis.

## ✨ Fitur Utama

- **🎙️ Transkripsi Real-time:** Mengubah audio panggilan darurat (Bahasa Indonesia) menjadi teks menggunakan Google Cloud Speech-to-Text.
- **🏷️ Klasifikasi Darurat Otomatis:** Menggunakan model Transformer (IndoBERT) yang telah di-*fine-tuning* untuk mengkategorikan jenis insiden (Medis, Kebakaran, Kriminal, dll.).
- **📍 Ekstraksi Entitas (NER):** Mengidentifikasi dan mengekstrak informasi kunci seperti lokasi dan objek penting dari teks panggilan.
- **🔌 API Siap Pakai:** Menyediakan semua fungsionalitas di atas melalui endpoint RESTful API yang dibuat dengan FastAPI, siap untuk diintegrasikan dengan aplikasi frontend.

## 🛠️ Tech Stack

- **Backend:** FastAPI, Uvicorn
- **AI / Machine Learning:**
  - **Speech-to-Text:** Google Cloud Speech-to-Text
  - **NLP (NER & Klasifikasi):** Hugging Face Transformers, PyTorch
  - **Model yang Digunakan:** `indobenchmark/indobert-base-p1`, `cahya/bert-base-indonesian-ner`
- **Pemrosesan Audio:** gTTS (untuk data sintetik), FFmpeg
- **Utility:** Pandas, Scikit-learn

## ⚙️ Panduan Setup dan Instalasi

Berikut adalah cara untuk menjalankan API ini di lingkungan lokal.

### 1. Prasyarat
- **Python 3.10+**
- **Git**
- **FFmpeg:** Pastikan FFmpeg sudah terinstal dan ditambahkan ke PATH sistem Anda. (Lihat [panduan instalasi FFmpeg](https://www.gyan.dev/ffmpeg/builds/)).

### 2. Instalasi Proyek
```bash
# 1. Clone repositori ini
git clone https://github.com/USERNAME/NAMA-REPO.git
cd NAMA-REPO

# 2. Buat dan tempatkan file kredensial Google Cloud Anda
# Buat file bernama gcp-credentials.json dan letakkan di folder root proyek ini.
# File ini TIDAK akan diunggah ke GitHub (sudah ada di .gitignore).

# 3. Buat dan aktifkan virtual environment
python -m venv venv
# Untuk Windows:
venv\Scripts\activate
# Untuk macOS/Linux:
# source venv/bin/activate

# 4. Instal semua dependensi yang dibutuhkan
pip install -r requirements.txt```

### 3. Menjalankan Server API
```bash
# Masuk ke direktori api
cd api

# Jalankan server menggunakan Uvicorn
uvicorn main:app --reload