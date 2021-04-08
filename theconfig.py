import os

"""For Heroku"""

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

"""
For Local Host

API_ID = 69
API_HASH = "ABCD1245"
BOT_TOKEN = "17383:idjeksjs"

"""