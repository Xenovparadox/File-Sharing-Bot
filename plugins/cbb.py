#(©)Codexbotz

from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : @Xenov7x\n○ Language : <code>Python3</code>\n○ Source Code : <a href='https://telegram.me/Sn_botsupport'>Available</a>\n○ Channel : @SupernovaNetwork\n○ Support Group : <a href='https://telegram.me/anime_supernova_chat'>This Channel</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗿 Close", callback_data = "close")
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
