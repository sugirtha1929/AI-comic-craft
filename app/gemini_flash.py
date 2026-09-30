import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_outline(
    story_prompt,
    character_name,
    setting,
    tone,
    art_style
):
    prompt = f"""
You are an expert comic story planner.

Create a 5-panel comic outline using the following details.

Story Prompt:
{story_prompt}

Main Character:
{character_name}

Setting:
{setting}

Tone:
{tone}

Art Style:
{art_style}

Return ONLY valid JSON.

The JSON must have this structure:

[
    {{
        "panel": 1,
        "title": "Panel title",
        "scene_description": "Description of the scene",
        "image_prompt": "Detailed prompt for image generation"
    }}
]

Create exactly 5 panels.
Make the story continuous from panel 1 to panel 5.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown formatting if Gemini returns it
    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "")

    return json.loads(text.strip())