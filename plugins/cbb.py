#(©)projectcrown

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""
   : {}
  : <a href=https://t.me/projectcrown>  </a> 
  : <a href=https://t.me/little_little_hackur> </a>
  : <a href=https://github.com/pyrogram></a>
  : <a href=https://www.python.org> 3</a>
   : <a href=https://cloud.mongodb.com></a>
   : <a href=https://mogenius.com/home></a>
   : v3.6.8 [  ]              

""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ðŸ”’ Close", callback_data = "close")
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