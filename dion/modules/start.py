# ⚠️ If you don't want /start in your bot
# you can delete this file 

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from dion import app
from dion.utils.filters import command
from dion.config import BOT_USERNAME, BOT_NAME, SUPPORT, UPDATE


home_text_pm = (
    f"Hey there! My name is {BOT_NAME}. I can play music on"
    + "group with lots of useful commands, feel free to "
    + "add me to your group. Type /help to see the commands"
)

keyboard_pm = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Add Me To Your Group 🎉",
                url=f"http://t.me/{BOT_USERNAME}?startgroup=kontol",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Updates 💻",
                url=f"t.me/{UPDATE}",
            ),
            InlineKeyboardButton(text="Support 📢", url=f"t.me/{SUPPORT}"),
        ],
        [
            InlineKeyboardButton(
                text="Repo 🛠",
                url="https://github.com/SeorangDion/DionMusicBot",
            ),
        ],
    ]
)


@app.on_message(command(["start"]) & filters.private & ~filters.edited)
async def start(_, message):
    await message.reply(
            home_text_pm,
            reply_markup=keyboard_pm,
        )

    
@app.on_message(command("help") & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.mention()}, this is all my commands!
\nFor Members:
/play (song title/link/audio) — To Play the song you requested via YouTube
/song (song title) - To Download songs from YouTube
/search (video title) — To Search Videos on YouTube with details
\n**Admins Only:**
/pause - To Pause Song playback
/resume - To resume playback of the paused song
/skip - To Skip playback of the song to the next Song
/end - To Stop Song playback
/cleandb - To clear all queues
/userbotjoin - To Invite assistant to your chat
/userbotleave - To remove assistant from your chat
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰 Updates", url=f"https://t.me/{UPDATE}"
                    ),
                    InlineKeyboardButton(
                        "📢 Support", url=f"https://t.me/{SUPPORT}"
                    ),
                ]
            ]
        )
    )
