import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_story(outline):

    prompt = f"""
You are a professional comic book writer.

Using the following 5-panel outline, create a complete comic story.

OUTLINE:
{outline}

For every panel provide:

Panel Number
Title
Narration
Caption
Character Dialogue

Make the story:
- Creative
- Easy to understand
- Connected between panels
- Suitable for a comic book
- Engaging

Clearly separate each panel.
"""

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    return response.text