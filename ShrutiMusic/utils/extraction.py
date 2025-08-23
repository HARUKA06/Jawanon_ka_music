from pyrogram.enums import MessageEntityType
from pyrogram.types import Message, User

from ShrutiMusic import app


async def extract_user(m: Message) -> User:
    if m.reply_to_message:
        return m.reply_to_message.from_user
    msg_entities = m.entities[1] if m.text.startswith("/") else m.entities[0]
    return await app.get_users(
        msg_entities.user.id
        if msg_entities.type == MessageEntityType.TEXT_MENTION
        else int(m.command[1])
        if m.command[1].isdecimal()
        else m.command[1]
    )


# ©️ Copyright Reserved -HARUKA06/Jawanon_ka_music

# ===========================================
# 🔗 GitHub : https://github.com/HARUKA06/Jawanon_ka_music
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From Jawanon_ka_music
