"""
Maintain, Telegram Maintain Bot

Copyright (C) 2021 Vivek-TP <https://t.me/Vivek_Kerala>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""
import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
    "Maintain-Bot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)

updatesc = os.environ["UPDATES_CHANNEL"]
supportc = os.environ["SUPPORT_CHAT"]

BOT_TEXT = """
Hai {} , This Bot Is Under Maintenance.

You Can't Use This Bot Right Now.You Will Get a Message On This Bot's Channel If This Bot Is Ready To Work.
"""

BOT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Channel", url=f"https://telegram.me/{updatesc}"),
            InlineKeyboardButton(text="Support", url=f"https://telegram.me/{supportc}"),
        ]
    ]
)


@Bot.on_message(filters.private)
async def start(bot, update):
    text = BOT_TEXT.format(update.from_user.mention)
    reply_markup = BOT_BUTTONS
    await update.reply_text(
        text=text, disable_web_page_preview=True, reply_markup=reply_markup
    )

print(
    """
Bot Started!!! Now Join on @Vkprojects
"""
)

Bot.run()

@Client.on_message(filters.command(["repo"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('𝒉𝒐𝒎𝒆', callback_data='start'),
        InlineKeyboardButton('𝒄𝒍𝒐𝒔𝒆 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.REPO_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
