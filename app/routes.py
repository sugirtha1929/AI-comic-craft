from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from .gemini_flash import generate_outline
from .gemini_pro import generate_story
from .image_generator import generate_image
from .layout_builder import build_comic_layout
from .exporters import save_pdf


router = APIRouter()

templates = Jinja2Templates(directory="templates")


# ---------------------------------------
# HOME PAGE
# ---------------------------------------
@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# ---------------------------------------
# GENERATE COMIC
# ---------------------------------------
@router.post("/generate")
async def generate_comic(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):

    # Step 1: Generate 5-panel outline using Gemini Flash
    outline = generate_outline(
        story_prompt,
        character_name,
        setting,
        tone,
        art_style
    )

    layout = []

    # Step 2: Generate story + images for each panel
    for panel in outline:

        story = generate_story(
            panel,
            character_name,
            tone
        )

        image_path = generate_image(
            panel["image_prompt"],
            panel["panel"]
        )

        layout.append({
            "panel": panel["panel"],
            "title": panel["title"],
            "scene_description": panel["scene_description"],
            "story": story,
            "image": "/" + image_path.replace("\\", "/")
        })

    # Step 3: Create PDF
    pdf_path = save_pdf(layout)

    # Step 4: Show comic preview
    return templates.TemplateResponse(
        request=request,
        name="comic_preview.html",
        context={
            "layout": layout,
            "pdf_path": "/" + pdf_path.replace("\\", "/")
        }
    )


# ---------------------------------------
# JSON API
# ---------------------------------------
@router.post("/generate-comic/json")
async def generate_comic_json(request: Request):

    data = await request.json()

    story_prompt = data.get("story_prompt", "")
    character_name = data.get("character_name", "Hero")
    setting = data.get("setting", "Fantasy")
    tone = data.get("tone", "Adventure")
    art_style = data.get("art_style", "Comic Book")

    outline = generate_outline(
        story_prompt,
        character_name,
        setting,
        tone,
        art_style
    )

    return {
        "success": True,
        "outline": outline
    }


# ---------------------------------------
# TEST IMAGE
# ---------------------------------------
@router.get("/test-image")
async def test_image():

    image_path = generate_image(
        "A colorful superhero standing in a futuristic city",
        1
    )

    return {
        "success": True,
        "image": "/" + image_path.replace("\\", "/")
    }


# ---------------------------------------
# EXPORT SUCCESS
# ---------------------------------------
@router.get("/export-success")
async def export_success(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="export_success.html",
        context={}
    )