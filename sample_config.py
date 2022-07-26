from os import environ

from dotenv import load_dotenv

load_dotenv("config.env")

HEROKU = bool(
    environ.get("DYNO")
)  # NOTE Make it false if you're not deploying on heroku or docker.

if HEROKU:

    BOT_TOKEN = environ.get("BOT_TOKEN", None)
    API_ID = int(environ.get("API_ID", 6))
    API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    SESSION_STRING = environ.get("SESSION_STRING", None)
    USERBOT_PREFIX = environ.get("USERBOT_PREFIX", ".")
    SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "").split()]
    LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))
    GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", None))
    MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", None))
    WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", None))
    MONGO_URL = environ.get("MONGO_URL", None)
    ARQ_API_URL = environ.get("ARQ_API_URL", None)
    ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
    LOG_MENTIONS = bool(int(environ.get("LOG_MENTIONS", None)))
    RSS_DELAY = int(environ.get("RSS_DELAY", None))
    PM_PERMIT = bool(int(environ.get("PM_PERMIT", None)))
else:
    BOT_TOKEN = "5570459431:AAFkMKp9W4AOaUyvu8_YbpZxY0C4b0slyIQ"
    API_ID ="2370938"
    API_HASH = "28ea568cb7ac6cbf1291799e0e2c77d2"
    USERBOT_PREFIX = ".sh"
    PHONE_NUMBER = "+916909292139"  # Need for Userbot
    SUDO_USERS_ID = [
        1382148141,
    ]  # Sudo users have full access to everything, don't trust anyone
    LOG_GROUP_ID = -1001727551382
    GBAN_LOG_GROUP_ID = -628808052
    MESSAGE_DUMP_CHAT = -1001727551382
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_URL = "mongodb+srv://sangteiubot:sangteiubot@cluster0.hnd2z.mongodb.net/?retryWrites=true&w=majority"
    ARQ_API_KEY = "HAGPNZ-MXGLCP-JEFIAL-XVBZJG-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    LOG_MENTIONS = True
    RSS_DELAY = 300  # In seconds
    PM_PERMIT = True
