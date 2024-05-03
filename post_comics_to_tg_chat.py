import os
import requests
import telegram
import fetch_image_utils as common
import fetch_xkcd_comics as xkcd
from dotenv import load_dotenv
from pathlib import Path

if __name__ == "__main__":
    Path(common.IMAGE_FOLDER).mkdir(parents=True, exist_ok=True)
    load_dotenv()
    filename = xkcd.fetch_comics()
    if common.check_file_size(filename):
        bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
        try:
            with open(f"{common.IMAGE_FOLDER}{filename}", "rb") as file:
                bot.send_document(chat_id=os.environ["TELEGRAM_CHAT_ID"], document=file)
            print("The comics has been successfully posted to telegram")
        except requests.HTTPError:
            print("Post comics error - check the validity of token and chat-id")
        finally:
            os.remove(f"{common.IMAGE_FOLDER}{filename}")