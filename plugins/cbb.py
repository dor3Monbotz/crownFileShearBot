#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "":
        await query.message.edit_text(
            text = f"<b>○  : <a href='tg://user?id={OWNER_ID}'>s s</a>\n○  : <code>Python3</code>\n○  : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ s  : <a href='https://github.com/dor3Monbotz/crownFileShearBot'> </a>\n○  : @projectcrown\n○ s  : https://t.me/crownbotzsupport</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("s", callback_data = "close")
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