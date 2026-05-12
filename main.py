import asyncio
import os
from flask import Flask
from bot import Bot
import threading

# 1. Setup Flask to keep Pella happy
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    # Pella uses port 8080 by default (check your screenshot)
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# 2. Setup your Pyrogram Bot
async def start_bot():
    bot = Bot()
    await bot.start()
    print("Bot started successfully!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    # Run Flask in a separate thread so it doesn't block the bot
    threading.Thread(target=run_flask, daemon=True).start()
    
    # Run the Pyrogram bot
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        pass
        
