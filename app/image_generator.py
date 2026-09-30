import os
import uuid
import torch

from diffusers import StableDiffusionPipeline


MODEL_ID = "runwayml/stable-diffusion-v1-5"

device = "cuda" if torch.cuda.is_available() else "cpu"


print("Loading Stable Diffusion model...")

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID
)

pipe = pipe.to(device)

print("Stable Diffusion loaded.")


def generate_image(prompt):

    os.makedirs(
        "static/panels",
        exist_ok=True
    )

    full_prompt = f"""
    {prompt},
    comic book illustration,
    detailed,
    cinematic lighting,
    colorful,
    high quality,
    consistent character design
    """

    image = pipe(
        full_prompt,
        num_inference_steps=25
    ).images[0]

    filename = f"comic_panel_{uuid.uuid4().hex}.png"

    filepath = os.path.join(
        "static",
        "panels",
        filename
    )

    image.save(filepath)

    return f"static/panels/{filename}"