# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


from Jawanon_ka_music.core.bot import Aviax
from Jawanon_ka_music.core.dir import dirr
from Jawanon_ka_music.core.git import git
from Jawanon_ka_music.core.userbot import Userbot
from Jawanon_ka_music.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# 🔗 GitHub : None
# 📢 Telegram Channel : https://t.me/Jawanon_ka_adda
# ===========================================


# ❤️ Love From Jawanon_ka_music 
