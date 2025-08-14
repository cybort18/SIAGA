# SIAGA 112: AI Emergency Call Triage System

**A project for the AI Innovation Challenge - COMPFEST 17**
**Theme: Smart City and Urban Living**

---

## 📝 Project Overview

SIAGA 112 is an AI-powered system designed to act as the first layer in handling emergency calls in dense urban environments like Jakarta. This project aims to enhance the efficiency and response speed of emergency services by automatically triaging incoming calls. The system transforms raw audio input into structured, actionable data that can be immediately processed.

## 🛠️ Tech Stack & Architecture

This project consists of several key components working together to create a complete AI pipeline.

**1. AI Backend (This Repository):**
*   **Framework:** FastAPI
*   **Server:** Uvicorn
*   **Speech-to-Text (STT):** Google Cloud Speech-to-Text API
*   **Natural Language Processing (NLP):**
    *   **Text Classification:** A fine-tuned `indobenchmark/indobert-base-p1` model using the Hugging Face Transformers library.
    *   **Named Entity Recognition (NER):** Leveraging the pre-trained `cahya/bert-base-indonesian-ner` model from the Hugging Face Hub.

**2. Frontend:**
*   (e.g., Next.js & Tailwind CSS)

**3. UI/UX:**
*   (e.g., Figma)

## 🧠 AI Workflow

The AI pipeline processes data through the following workflow:

1.  **Audio Ingestion:** Receives an audio file (e.g., `.wav`, `.mp3`) from a user via an API endpoint.
2.  **Speech-to-Text (STT):** The audio file is sent to the Google Cloud Speech-to-Text API for transcription into Indonesian text.
3.  **NLP Analysis:** The resulting text is processed by two parallel AI models:
    *   **Classification Model:** Determines the emergency category (e.g., Medical, Fire, Criminal).
    *   **NER Model:** Extracts key entities such as location (LOK), objects (OBJ), etc.
4.  **JSON Formatting:** The analysis results (transcription, category, entities) are structured into a clean JSON payload.
5.  **API Response:** The JSON payload is sent back to the frontend for display to the user or an operator.

## 🚀 Getting Started

Follow these steps to set up and run the AI server locally.

### Prerequisites

*   [Git](https://git-scm.com/downloads)
*   [Python](https://www.python.org/downloads/) (3.9+ recommended)
*   [FFmpeg](https://www.gyan.dev/ffmpeg/builds/): Download the essentials build, extract it, and add its `bin` folder to your system's PATH.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/[YOUR_GITHUB_USERNAME]/[YOUR_REPO_NAME].git
    cd [YOUR_REPO_NAME]
    ```

2.  **Create & Activate a Virtual Environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Google Cloud Credentials:**
    *   In the Google Cloud Console, create a new service account and enable the **Cloud Speech-to-Text API**.
    *   Download the API key for the service account in JSON format.
    *   Rename the downloaded key to `gcp-credentials.json` and place it in the **root directory** of this project (the same location as this README file). This file is already listed in `.gitignore` and will not be uploaded.

## ▶️ Running the Application

1.  **(Optional) Generate Synthetic Data:**
    *   To regenerate the text and audio data, run the Jupyter Notebook at `notebooks/01_data_preparation.ipynb`.

2.  **(Optional) Retrain the Classification Model:**
    *   To fine-tune the classification model again, run the Jupyter Notebook at `notebooks/03_classification_training.ipynb`.

3.  **Run the API Server:**
    *   Navigate to the `api/` directory and start the server using Uvicorn.
    ```bash
    cd api
    uvicorn main:app --reload
    ```
    *   The server will be available at `http://127.0.0.1:8000`.
    *   Interactive API documentation (via Swagger UI) is available at `http://127.0.0.1:8000/docs`.
