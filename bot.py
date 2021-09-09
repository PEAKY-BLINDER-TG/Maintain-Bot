from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation

bot = Client(
  "message-bot",
  bot_token="1943952420:AAG4yAPtx_vlFSoXa7yzDhe4xcWKenTEfMA",
  api_id="3020564",
  api_hash="91c026fadfdc442f504a0bd3e5c8cd18",
  )

API_TEXT = """🙋‍♂ **Hi {},**
**I am a String Session generator bot.**
**For generating string session send me your** `API_ID` 🐿
𝐂𝐫𝐞𝐚𝐭𝐨𝐫 [peaky-blinder](https://t.me/no_ones_like_me)
"""

@bot.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(
        text=API_TEXT.format(m.from_user.mention(style='md')),
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
        )
bot.run()
