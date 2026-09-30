def build_comic_layout(
    outline,
    story,
    images
):

    layout = []

    # Split generated story
    story_sections = story.split("\n\n")

    for index, panel in enumerate(outline):

        if index < len(story_sections):
            panel_story = story_sections[index]
        else:
            panel_story = ""

        layout.append({
            "panel": panel["panel"],
            "title": panel["title"],
            "scene_description":
                panel["scene_description"],
            "image":
                "/" + images[index].replace("\\", "/"),
            "story":
                panel_story
        })

    return layout