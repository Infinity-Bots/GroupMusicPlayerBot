from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

Saya bisa memutarkan musik di group anda dengan nyaman,penghantar tidur juga tapi gak bisa ngisi hati kalian. Manage by [ᴇxᴇᴄᴜᴛᴏʀ](https://t.me/penjelajahdimensi).

Tambahkan saya ke group untuk menikmati alunan musiknya!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌬 Group Support", url="https://t.me/thisrevolution")
                  ],[
                    InlineKeyboardButton(
                        "📸 Owner Fake", url="https://t.me/penjelajahdimensi"
                    ),
                    InlineKeyboardButton(
                        "💕 Suara Isi Hati 💕", url="https://t.me/OfiicialRevolution"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/MemewMusicbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💞 Suara Isi Hati 💕", url="https://t.me/ohempty")
                ]
            ]
        )
   )


