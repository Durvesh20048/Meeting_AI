# 🤖 AI Meeting Assistant

> **Transform meeting audio into intelligent summaries, key insights, and actionable decisions using AI-powered Speech-to-Text and Large Language Models.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi"/>
  <img src="https://img.shields.io/badge/Whisper-Speech--to--Text-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Ollama-LLM-black?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/HTML-CSS-JS-orange?style=for-the-badge"/>
</p>

---

# 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Objectives](#-objectives)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Project Workflow](#-project-workflow)
- [Tech Stack](#-tech-stack)
- [AI Concepts Used](#-ai-concepts-used)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Resources Used](#-resources-used)
- [Challenges Faced](#-challenges-faced)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- [License](#-license)

---

# 📖 Project Overview

AI Meeting Assistant is an end-to-end AI application that automatically converts meeting recordings into structured meeting notes.

The system processes uploaded audio files, converts speech into text using Whisper Speech-to-Text, and generates intelligent meeting summaries, key discussion points, and action items using Large Language Models.

The project demonstrates practical implementation of modern AI pipelines, REST API development, audio processing, prompt engineering, and frontend-backend integration.

---

# 🎯 Objectives

- Automate meeting documentation
- Reduce manual note-taking
- Generate structured meeting summaries
- Extract important discussion points
- Identify action items
- Build an end-to-end AI workflow
- Demonstrate modern AI application development

---

# ✨ Key Features

- 🎙 Upload meeting audio files
- 📄 Automatic Speech-to-Text transcription
- 🤖 AI-generated meeting summary
- ✅ Action Item Extraction
- 📌 Key Discussion Points
- 🎨 Modern responsive UI
- 📂 Multiple audio format support
- 🔄 Automatic audio conversion
- ⚡ FastAPI backend
- 🌐 REST API architecture
- 🔒 Local AI processing (Whisper + Ollama)

---

# 🏗 System Architecture

```text
                User

                  │

          Upload Audio File

                  │

         HTML • CSS • JavaScript

                  │
        REST API Request (POST)

                  │

             FastAPI Backend

                  │

       Audio Preprocessing (FFmpeg)

                  │

          Whisper Speech Model

                  │

          Transcript Generation

                  │

          Ollama (TinyLlama)

                  │

      Prompt Engineering Pipeline

                  │

      Summary + Insights + Actions

                  │

        JSON Response to Frontend

                  │

          Beautiful User Interface
```

---

# 🔄 Project Workflow

### Step 1

User uploads an audio recording.

↓

### Step 2

Backend receives the file through FastAPI.

↓

### Step 3

Audio is converted into WAV format using FFmpeg.

↓

### Step 4

Whisper transcribes speech into text.

↓

### Step 5

Transcript is passed to the Large Language Model.

↓

### Step 6

Prompt Engineering guides the model to generate:

- Summary
- Key Points
- Action Items

↓

### Step 7

Frontend displays formatted AI results.

---

# 💻 Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript

---

## Backend

- Python
- FastAPI
- Uvicorn

---

## Artificial Intelligence

- OpenAI Whisper
- Ollama
- TinyLlama
- Prompt Engineering
- NLP
- Speech-to-Text
- Large Language Models (LLMs)

---

## Audio Processing

- FFmpeg

---

## Deployment

- Netlify (Frontend)
- GitHub
- Render (Cloud-ready backend)

---

## Version Control

- Git
- GitHub

---

## Development Tools

- VS Code
- Postman / Swagger UI
- Virtual Environment (venv)

---

# 🧠 AI Concepts Used

- Natural Language Processing (NLP)
- Large Language Models (LLMs)
- Speech-to-Text (STT)
- Prompt Engineering
- Text Summarization
- Audio Processing
- REST API Integration
- Client-Server Architecture
- AI Pipeline Design
- Context-based Text Generation

---

# 📁 Project Structure

```text
Meeting_AI/

│
├── UI/
│ ├── landing.html
│ ├── index.html
│ ├── images/
│
├── app.py
├── analyzer.py
├── STT.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── audio_files/
│
└── venv/
```

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/YourUsername/Meeting_AI.git
```

Move into Project

```bash
cd Meeting_AI
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Backend

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

or launch the frontend UI.

---

# 🚀 Usage

1. Open the application.
2. Upload a meeting audio file.
3. Wait for transcription.
4. AI processes the transcript.
5. View:
   - Transcript
   - Summary
   - Key Points
   - Action Items

---

# 🌐 API Endpoints

### Upload Audio

```
POST /upload
```

Returns

```json
{
  "transcript": "...",
  "analysis": "..."
}
```

---

# 📚 Resources Used

## Documentation

- FastAPI Documentation
- OpenAI Whisper Documentation
- Ollama Documentation
- FFmpeg Documentation
- Python Official Documentation
- MDN Web Docs

---

## AI Models

- Whisper
- TinyLlama
- Ollama Runtime

---

## Libraries

- FastAPI
- Uvicorn
- Requests
- FFmpeg
- Python Standard Library

---

## Tools

- GitHub
- VS Code
- Netlify
- Render
- Swagger UI

---

# ⚡ Challenges Faced

- Audio format compatibility
- Large model memory limitations
- CORS configuration
- Frontend-backend communication
- Prompt hallucination reduction
- Efficient audio preprocessing
- Deployment of AI models

---

# 🚀 Future Enhancements

- Multi-language transcription
- Speaker Diarization
- Real-time meeting transcription
- PDF Meeting Report Export
- Email Meeting Summary
- Calendar Integration
- Authentication & User Accounts
- Cloud GPU deployment
- Meeting History Dashboard
- RAG-powered meeting search

---

# 👨‍💻 Author

**Durvesh Rajesh Nayak**
* Give a star if u liked the project *

---

# 📄 License

This project is developed for educational and portfolio purposes.

---

# ⭐ One-Line Impact

> **An intelligent AI-powered meeting assistant that transforms raw conversations into actionable insights through Speech-to-Text and Large Language Models.**
