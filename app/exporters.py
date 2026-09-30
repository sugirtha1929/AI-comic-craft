import os
import uuid

from fpdf import FPDF


def save_pdf(layout):

    os.makedirs(
        "static/exports",
        exist_ok=True
    )

    filename = (
        f"comic_{uuid.uuid4().hex}.pdf"
    )

    filepath = os.path.join(
        "static",
        "exports",
        filename
    )

    pdf = FPDF()

    for panel in layout:

        pdf.add_page()

        # Title
        pdf.set_font(
            "Arial",
            "B",
            18
        )

        pdf.cell(
            0,
            12,
            f"Panel {panel['panel']}: {panel['title']}",
            ln=True
        )

        # Image
        image_path = panel["image"].lstrip("/")

        if os.path.exists(image_path):

            pdf.image(
                image_path,
                x=10,
                y=30,
                w=190
            )

        # Text
        pdf.set_y(145)

        pdf.set_font(
            "Arial",
            "",
            11
        )

        text = (
            panel["scene_description"]
            + "\n\n"
            + panel["story"]
        )

        # Avoid unsupported Unicode characters
        text = text.encode(
            "latin-1",
            "replace"
        ).decode("latin-1")

        pdf.multi_cell(
            0,
            7,
            text
        )

    pdf.output(filepath)

    return f"/static/exports/{filename}"