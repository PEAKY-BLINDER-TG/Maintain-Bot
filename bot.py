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

buttons = [[
        InlineKeyboardButton('⚠️  𝒋𝒐𝒊𝒏', url='https://t.me/cinemazilla'),
        InlineKeyboardButton('🕵‍♂ 𝒄𝒓𝒆𝒂𝒕𝒐𝒓', url='https://t.me/no_ones_like_me')
        ],[
        InlineKeyboardButton('💡 𝒉𝒆𝒍𝒑', callback_data="help"),
        InlineKeyboardButton('🔐 𝒄𝒍𝒐𝒔𝒆', callback_data="close")
        ]]
    
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

