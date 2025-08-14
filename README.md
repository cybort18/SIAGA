# PH-AIC: The AI Engine

**Project for the AI Innovation Challenge - COMPFEST 17**
**Theme: Smart City and Urban Living**

---

## 🌟 Project Overview

**PH-AIC (Project Hackathon - AI Innovation Comfest)** is an innovative AI-powered system designed to revolutionize how cities handle medical emergencies and public health incidents. Our vision is to create smarter, safer, and more resilient urban healthcare systems through real-time data analysis.

### The Role of this Repository

This repository contains the **standalone AI Engine** that serves as the "brain" for the PH-AIC project. It is a backend service responsible for all machine learning inference. It exposes a robust API that the main frontend application consumes.

*   **Frontend & Main Project Repository:** [Link to your teammate's GitHub repository here]

## 🧠 The AI Workflow

The AI Engine processes data through the following pipeline:

1.  **Audio Ingestion:** Receives an audio file (e.g., `.wav`, `.mp3`) from a client application via a POST request.
2.  **Speech-to-Text (STT):** The audio is transcribed into Indonesian text using the Google Cloud Speech-to-Text API.
3.  **Parallel NLP Analysis:** The resulting text is analyzed by two models simultaneously:
    *   **Classification Model:** A fine-tuned `indobenchmark/indobert-base-p1` model determines the emergency category (Medical, Fire, Criminal, etc.).
    *   **NER Model:** The pre-trained `cahya/bert-base-indonesian-ner` model extracts key entities like locations (LOK) and objects (OBJ).
4.  **Structured JSON Output:** The analysis results are formatted into a clean JSON payload.
5.  **API Response:** The JSON payload is sent back to the client, providing structured and actionable data.

## 🛠️ Technology Stack

*   **API Framework:** FastAPI
*   **Web Server:** Uvicorn
*   **Speech-to-Text (STT):** Google Cloud Platform
*   **NLP / Machine Learning:** Hugging Face Transformers, PyTorch
*   **Audio Processing:** FFmpeg
*   **Large File Management:** Git LFS

## 🚀 Getting Started

Follow these steps to set up and run the AI server locally.

### Prerequisites

*   [Git](https://git-scm.com/downloads)
*   [Python](https://www.python.org/downloads/) (3.9+ recommended)
*   [Git LFS (Large File Storage)](https://git-lfs.github.com/): Required for handling the large model files.
*   [FFmpeg](https://www.gyan.dev/ffmpeg/builds/): Download the essentials build, extract it, and add its `bin` folder to your system's PATH.

### Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/[YOUR_GITHUB_USERNAME]/[YOUR_REPO_NAME].git
    cd [YOUR_REPO_NAME]
    ```

2.  **Set Up Git LFS:**
    *   If you've just installed Git LFS, run `git lfs install` once.
    *   Pull the large model files from LFS storage:
    ```bash
    git lfs pull
    ```

3.  **Create & Activate a Virtual Environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set Up Google Cloud Credentials:**
    *   In the Google Cloud Console, create a service account and enable the **Cloud Speech-to-Text API**.
    *   Download the API key in JSON format.
    *   Rename it to `gcp-credentials.json` and place it in the project's **root directory**. This file is already in `.gitignore`.

## ▶️ Running the Application

1.  **(Optional) Data & Model Generation:**
    *   To regenerate the synthetic data, run the notebook at `notebooks/01_data_preparation.ipynb`.
    *   To retrain the classification model, run the notebook at `notebooks/03_classification_training.ipynb`.

2.  **Run the API Server:**
    *   Navigate to the `api/` directory and start the server using Uvicorn.
    ```bash
    cd api
    uvicorn main:app --reload
    ```
    *   The server will be available at `http://127.0.0.1:8000`.
    *   Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## 👥 Our Team

*   **Project Lead:** Muhammad Zaky Ramadhan
*   **AI Development:** Muhammad Zaky Ramadhan
*   **Fullstack Development:** Muhammad Faiqul Umam Dz.
*   **UI/UX Design:** Muhammad Aulia Addinul Haq

---
*PH-AIC AI Engine - Transforming Urban Emergency Response through AI*