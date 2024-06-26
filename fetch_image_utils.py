import requests
import os
from urllib.parse import urlparse, unquote

IMAGE_FOLDER = os.path.join(os.getcwd(), "images")
MAX_FILE_SIZE = 20000000


def get_file_extension(url):
    filename = unquote(urlparse(url).path)
    extension = os.path.splitext(filename)[1]
    return extension


def download_picture(url, path, file_name):
    payload = {}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(os.path.join(path, file_name), mode="wb") as file:
        file.write(response.content)


def check_file_size(filename):
    file_size = os.path.getsize(os.path.join(IMAGE_FOLDER, filename))
    if file_size < MAX_FILE_SIZE:
        return True
