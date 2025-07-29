# import os
# import random
# import json

# IMAGE_FOLDER = r"C:\Users\nikhi\Downloads\hamdan_youtube_uploader\images"
# CAPTION_FILE = r"C:\Users\nikhi\Downloads\hamdan_youtube_uploader\captions\captions_5000.json"

# def load_captions():
#     with open(CAPTION_FILE, "r", encoding="utf-8") as f:
#         return json.load(f)

# def pick_image_and_caption():
#     captions = load_captions()
#     images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

#     if not images:
#         raise ValueError("No images found in folder.")

#     image_file = random.choice(images)
#     caption = random.choice(captions)

#     image_path = os.path.join(IMAGE_FOLDER, image_file)
#     return image_path, caption

import os
import random
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGE_FOLDER = os.path.join(BASE_DIR, 'images')
CAPTION_FILE = os.path.join(BASE_DIR, 'captions', 'captions_5000.json')

def load_captions():
    if not os.path.exists(CAPTION_FILE):
        raise FileNotFoundError(f"Caption file not found: {CAPTION_FILE}")
    with open(CAPTION_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def pick_image_and_caption():
    if not os.path.isdir(IMAGE_FOLDER):
        raise FileNotFoundError(f"Image folder not found: {IMAGE_FOLDER}")
    
    captions = load_captions()
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not images:
        raise ValueError("No images found in folder.")

    image_file = random.choice(images)
    caption = random.choice(captions)

    image_path = os.path.join(IMAGE_FOLDER, image_file)
    return image_path, caption
