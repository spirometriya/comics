# Comics publisher
The script allows you to download random comics images from [xkcd.com](https://xkcd.com/) and post them to the telegram group.
The comics file will be deleted from the "images" folder of your project after publication.

# How to install

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

### Environment variables.

- TELEGRAM_TOKEN
- TELEGRAM_CHAT_ID

.env example:

```
TELEGRAM_TOKEN = "6417806071:5pAcwh9SoNqJAHsIUOsU7JbJ6MEXcKf1uUB"
TELEGRAM_CHAT_ID = "@dvmn_xkcd_comics"
```
### How to get

1. Register a new bot using a special bot [@BotFather](https://telegram.me/BotFather):
   - to create a new bot, send the command: /newbot
   - BotFather will prompt you to enter the name of the new bot and the username for the bot account
   - the name is displayed in the dialog box with the bot, and the username is used to link to it
   - the response message contains a token that is needed to control the bot via the API
2. Create a public group in telegram and a link to this group. A new bot must be added to this group with administrator rights.

### Run

Launch on Linux or Windows as simple

```bash
$ python post_comics_to_tg_chat.py

# Posts one random comics to your telegram group
# You will see

$ python post_comics_to_tg_chat.py
The comics has been successfully posted to telegram

# If the file size exceeds 20MB, the post request will not be executed!
```

# Project Goals

This code was written for educational purposes as part of an online course for web developers at dvmn.org.
