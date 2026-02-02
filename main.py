import os
import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
import yt_dlp

# ========== CONFIG ==========
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

# ========== CLIENTS ==========
bot = Client(
    "music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

user = Client(
    "music_user",
    api_id=API_ID,
    api_hash=API_HASH
)

call = PyTgCalls(user)

# ========== YOUTUBE ==========
def yt_audio(url):
    ydl_opts = {
        "format": "bestaudio",
        "quiet": True,
        "nocheckcertificate": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info["url"]

# ========== COMMANDS ==========
@bot.on_message(filters.command("start"))
async def start(_, m):
    await m.reply("🎧 VC Music Bot Online\n\n/play <youtube link>")

@bot.on_message(filters.command("play") & filters.group)
async def play(_, m):
    if len(m.command) < 2:
        return await m.reply("❌ /play <YouTube link>")

    chat_id = m.chat.id
    url = m.command[1]

    try:
        stream = yt_audio(url)
        await call.join_group_call(
            chat_id,
            AudioPiped(stream)
        )
        await m.reply("▶️ Playing in VC")

    except Exception as e:
        await m.reply(f"❌ Error: `{e}`")

@bot.on_message(filters.command("stop") & filters.group)
async def stop(_, m):
    try:
        await call.leave_group_call(m.chat.id)
        await m.reply("⏹ Stopped")
    except:
        await m.reply("❌ Nothing playing")

# ========== START ==========
async def main():
    await bot.start()
    await user.start()
    await call.start()
    print("🎵 VC Music Bot Started")
    await asyncio.Event().wait()

asyncio.run(main())
