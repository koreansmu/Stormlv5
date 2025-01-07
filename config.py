import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "23539804"
API_HASH = "a174f115853c3cc48b9d571329dd32f3"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7174246611:AAH9cXocdrT_xlSIcUXtpuYPNKP0C6ou6H4"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://fidixi3663:w7rvlxmDd5lsX9ix@cluster0.0k1an50.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 6000))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002068576120

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = 5960968099

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/CyberPixelPro/AviaxMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/STORM_TECHH")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/STORM_CORE")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-AviaxMusic-08-14")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFnMFwAgHmfwoNKs_8Canjb-yjh9xDk_G3hX3M7f_-C0aDSwcxpM1VfmLiSjcqhi_IaGEkXxFAZk-9ftQEXIQ2l85lK3INW7huiV3YUVl7e1V9oHf9K9VDvt4n9ko1BCLhTl7KYsPhCecPveJIanGsWQOVtv7WnFuctjEBGplexJlSopp2zR6gHULFAqcvs-sTytOjTebXh9or6iHaXXgqwMgZH0G5dT88paJ3rzyFg-9-S221NvK6Ja_m4CXokZooe3HpbM1LGdfveEdGk4jFuVAkKlE_OnNmAYcS6XyH4yzEnHngX0NgQYT5Og5lFaPNbLmbrkhoSUp6auB50cI-LiS7hOwAAAAHObTqWAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/2a8f51537c4b09def0b5a-686a24f38209600f34.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/61e2f285f190e8c67326a-c775c820c6850351ee.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/a674bdb80cac21aa940e3-7f9337f221f533888a.jpg"
STATS_IMG_URL = "https://graph.org/file/d27e3a4e6666c97e239e7-fd09816e4c54e7dc0c.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/c1733b944427e9d206369-150a4e4ba1752b4086.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/0e57a408587422ce7cd95-6c3eb9b7a0736300ed.jpg"
STREAM_IMG_URL = "https://graph.org/file/0e57a408587422ce7cd95-6c3eb9b7a0736300ed.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
