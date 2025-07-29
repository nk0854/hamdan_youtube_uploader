from poster import post_random_image
from time import sleep

for i in range(5):
    print(f"Posting image {i+1}...")
    post_random_image()
    sleep(10)
