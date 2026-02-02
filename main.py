import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from youtubesearchpython import VideosSearch
import yt_dlp

API_ID = 38063189
API_HASH = "1f5b2b7bd33615a2a3f34e406dd9ecab"
BOT_TOKEN = "8509750291:AAG54vnOJCjhATkJIkLxd1FJUZPkj10g3_o"

app = Client(
    "musicbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

call = PyTgCalls(app)

def yt_audio(query):
    search = VideosSearch(query, limit=1)
    result = search.result()["result"][0]["link"]

    ydl_opts = {
        "format": "bestaudio",
        "quiet": True,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(result, download=False)
        return info["url"]

@app.on_message(filters.command("play") & filters.group)
async def play(_, message):
    if not message.command[1:]:
        await message.reply("❌ Song name dao")
        return

    query = " ".join(message.command[1:])
    await message.reply("🔎 Searching...")

    audio = yt_audio(query)

    await call.join_group_call(
        message.chat.id,
        AudioPiped(audio, HighQualityAudio()),
    )

    await message.reply(f"▶️ Playing: **{query}**")

@app.on_message(filters.command("stop") & filters.group)
async def stop(_, message):
    await call.leave_group_call(message.chat.id)
    await message.reply("⏹ Stopped")

async def main():
    await app.start()
    await call.start()
    print("🎵 VC Music Bot Started")
    await asyncio.Event().wait()

asyncio.run(main())        info = ydl.extract_info(url, download=False)
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
