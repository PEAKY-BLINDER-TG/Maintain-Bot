from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation


@bot.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(
        text=hey how re youu,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("♻️ 𝙂𝙍𝙊𝙐𝙋", url="https://t.me/cinemazilla"),
                    InlineKeyboardButton("👨‍💻 𝙈𝘼𝙎𝙏𝙀𝙍", url="https://t.me/no_ones_like_me")
                ],
                [
                    InlineKeyboardButton("💿 𝙅𝙊𝙄𝙉 𝙊𝙐𝙍 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 💿", url="https://t.me/joinchat/CXRICR1ok3ViZjk9")
                ],
                [
                    InlineKeyboardButton("🔐 𝘾𝙇𝙊𝙎𝙀", url="https://t.me/joinchat/CXRICR1ok3ViZjk9"),
                    InlineKeyboardButton("💡𝙃𝙀𝙇𝙋", url="https://t.me/joinchat/CXRICR1ok3ViZjk9")
                ]
            ]
        ),
