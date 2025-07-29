from image_picker import pick_image_and_caption
from youtube_uploader import upload_to_youtube_community

def post_random_image():
    image_path, caption = pick_image_and_caption()
    upload_to_youtube_community(image_path, caption)
