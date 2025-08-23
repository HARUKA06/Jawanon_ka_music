from Jawanon_ka_music import app
from Jawanon_ka_music.utils.database import get_cmode


async def get_channeplayCB(_, command, CallbackQuery):
    if command == "c":
        chat_id = await get_cmode(CallbackQuery.message.chat.id)
        if chat_id is None:
            try:
                return await CallbackQuery.answer(_["setting_7"], show_alert=True)
            except:
                return
        try:
            channel = (await app.get_chat(chat_id)).title
        except:
            try:
                return await CallbackQuery.answer(_["cplay_4"], show_alert=True)
            except:
                return
    else:
        chat_id = CallbackQuery.message.chat.id
        channel = None
    return chat_id, channel


# ©️ Copyright Reserved - HARUKA06/Jawanon_ka_music

# ===========================================
# 🔗 GitHub : https://github.com/HARUKA06/Jawanon_ka_music
# 📢 Telegram Channel : https://t.me/Jawanon_ka_music
# ===========================================


# ❤️ Love From Jawanon_ka_music
