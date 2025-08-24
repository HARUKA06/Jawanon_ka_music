
import os

from ..logging import LOGGER


def dirr():
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
        elif file.endswith(".jpeg"):
            os.remove(file)
        elif file.endswith(".png"):
            os.remove(file)

    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")

    LOGGER(__name__).info("Directories Updated.")


# ©️ Copyright Reserved - 

# ===========================================
# ©️ 2025 Nand HARUKA06/Jawanon_ka_music
# 🔗 GitHub : https://github.com/HARUKA06/Jawanon_ka_music
# 📢 Telegram Channel : https://t.me/Jawanon_ka_adda
# ===========================================


# ❤️ Love From Jawanon_ka_music
