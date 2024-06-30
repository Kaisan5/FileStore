#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ᴋᴀɪ</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Eternals'>ᴀɴɪᴍᴇ ᴇᴛᴇʀɴᴀʟꜱ</a>\n○  ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ: <a href='https://t.me/Anime_Ongoing_Airings'>ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢꜱ</a>\n○ ɢʀᴏᴜᴘ ᴄʜᴀᴛ: <a href='https://t.me/AnimeChatNexus'>ɴᴇxᴜꜱ ᴄʜᴀᴛ</a>\n○ ɴᴇᴛᴡᴏʀᴋ: <a href='https://t.me/AnimeNexusNetwork'>ᴀɴɪᴍᴇ ɴᴇxᴜꜱ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴇᴛᴇʀɴᴀʟꜱ', url='https://t.me/Anime_Eternals')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
