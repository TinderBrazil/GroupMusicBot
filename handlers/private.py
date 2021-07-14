from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAECeu5g1jbudQdfsILsLCDRQKxTDs5-LwACigEAAo7fCEXnX3pqsrzPnSAE")
    await message.reply_text(
        f"""**Ei eu sou {bn} 🎵

Posso tocar música na chamada de voz do seu grupo. Desenvolvido por [Tio Morty](https://t.me/TioMorty).

Adicione-me ao seu grupo e toque música de graça!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Criador", url="https://t.me/TioMorty")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/TheRealVibes"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/TiuMorty"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Adicionar ao seu grupo ➕", url="https://t.me/TioMortyBot?startgroup=true"
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
                        "🔊 Channel", url="https://t.me/DextyPlayer")
                ]
            ]
        )
   )


