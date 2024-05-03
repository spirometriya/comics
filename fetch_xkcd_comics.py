import fetch_image_utils as common
import random
import requests

LAST_COMICS_URL = "https://xkcd.com/info.0.json"
COMICS_URL_BY_ID = "https://xkcd.com/{}/info.0.json"


def get_random_comics_id():
    response = requests.get(LAST_COMICS_URL)
    response.raise_for_status()
    total_comics = response.json().get("num")
    return random.randint(1, total_comics)


def fetch_comics(comics_id):
    response = requests.get(COMICS_URL_BY_ID.format(comics_id))
    response.raise_for_status()
    url = response.json().get("img")
    extension = common.get_file_extension(url)
    filename = f"{comics_id}{extension}"
    common.download_picture(url, common.IMAGE_FOLDER, filename)
    return filename
