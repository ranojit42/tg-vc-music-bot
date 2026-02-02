import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from yt_dlp import YoutubeDL

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SESSION = os.environ.get("SESSION")

app = Client(
    "musicbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

user = Client(
    SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
)

call = PyTgCalls(user)

ydl_opts = {"format": "bestaudio"}

@app.on_message(filters.command("start"))
async def start(_, m):
    await m.reply("🎵 VC Music Bot Ready!")

@app.on_message(filters.command("play") & filters.group)
async def play(_, m):
    if len(m.command) < 2:
        return await m.reply("❌ Song name দাও")

    query = " ".join(m.command[1:])
    msg = await m.reply("🔍 Searching...")

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)["entries"][0]
        url = info["url"]

    await call.join_group_call(
        m.chat.id,
        AudioPiped(url, HighQualityAudio()),
    )
    await msg.edit(f"▶️ Playing: {info['title']}")

@app.on_message(filters.command("stop"))
async def stop(_, m):
    await call.leave_group_call(m.chat.id)
    await m.reply("⏹ Stopped")

async def main():
    await app.start()
    await user.start()
    await call.start()
    print("Bot started")
    await idle()

if __name__ == "__main__":
    import asyncio
    from pyrogram import idle
    asyncio.get_event_loop().run_until_complete(main())
