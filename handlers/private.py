from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker(" CAACAgIAAx0CVsbI6AACPwNgqWejAzgsQRKlL-mSyw3uttDMDQACYjcAAuCjggcSvw6d3PYOgR8E")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

        I can play music in your group's voice call.
currently playing on [Anime Loverz](https://t.me/animeloversreborn).


        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/Infinity-Bots/GroupMusicPlayerBot")
                  ],[
                    InlineKeyboardButton(
                        "Group", url="https://t.me/animeloversreborn"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="sanjitsinha"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true"
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
                        "How to use", url="https://telegra.ph/file/cee4383ec7a5c19be9590.jpg")
                ]
            ]
        )
   )


