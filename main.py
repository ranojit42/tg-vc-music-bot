import os
import asyncio
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message

# ================== CONFIG ==================

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "")  # like -100xxxxxxx or @channelusername

if not all([API_ID, API_HASH, BOT_TOKEN, CHANNEL_ID]):
    print("❌ Missing environment variables")
    print("Set: API_ID, API_HASH, BOT_TOKEN, CHANNEL_ID")
    exit(1)

# ================== BOT ==================

app = Client(
    "vip_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ================== COMMANDS ==================

@app.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text(
        "👋 **Welcome!**\n\n"
        "This is a **VIP Telegram Bot**.\n"
        "All replies are in English.\n\n"
        "Type /help to see available commands."
    )

@app.on_message(filters.command("help"))
async def help_cmd(_, message: Message):
    await message.reply_text(
        "📌 **Available Commands**\n\n"
        "/start - Start the bot\n"
        "/help - Show help\n"
        "/ping - Check bot status\n"
    )

@app.on_message(filters.command("ping"))
async def ping(_, message: Message):
    await message.reply_text("🏓 Pong! Bot is running perfectly.")

# ================== DAILY POST ==================

async def daily_post():
    await app.wait_until_ready()
    while True:
        try:
            text = (
                "📢 **Daily VIP Update**\n\n"
                f"🕒 Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                "🔥 Stay tuned for more updates!\n"
                "🚀 Powered by VIP Bot"
            )
            await app.send_message(CHANNEL_ID, text)
            print("✅ Daily post sent")
        except Exception as e:
            print("❌ Daily post error:", e)

        await asyncio.sleep(86400)  # 24 hours

# ================== START ==================

async def main():
    await app.start()
    print("🤖 VIP Bot Started")
    asyncio.create_task(daily_post())
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
if __name__ == "__main__":
    import asyncio
    from pyrogram import idle
    asyncio.get_event_loop().run_until_complete(main())
