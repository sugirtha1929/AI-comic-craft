# ComicCraft

## AI Comic Story Creator using Gemini Models

ComicCraft is an AI-powered web application that converts
user story ideas into complete comic stories.

## Technologies

- Python
- FastAPI
- HTML
- CSS
- Jinja2
- Gemini AI
- Stable Diffusion
- FPDF

## AI Workflow

1. User enters comic details.
2. Gemini Flash creates a 5-panel outline.
3. Gemini Pro generates narration and dialogue.
4. Stable Diffusion generates comic images.
5. Layout Builder combines text and images.
6. FPDF creates the final PDF.
7. User downloads the comic.

## Installation

Create virtual environment:

python -m venv env

Activate on Windows:

env\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Run

uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs