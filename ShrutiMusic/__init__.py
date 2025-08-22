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
