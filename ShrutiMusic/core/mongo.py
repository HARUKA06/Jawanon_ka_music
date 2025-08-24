
from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Connecting to your Mongo Database...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Yukki
    LOGGER(__name__).info("Connected to your Mongo Database.")
except:
    LOGGER(__name__).error("Failed to connect to your Mongo Database.")
    exit()


# ©️ Copyright Reserved - 

# ===========================================
# ©️ 2025 Nand HARUKA06/Jawanon_ka_music
# 🔗 GitHub : https://github.com/HARUKA06/Jawanon_ka_musicutiMusic
# 📢 Telegram Channel : https://t.me/Jawanon_ka_adda
# ===========================================


# ❤️ Love From Jawanon_ka_music
