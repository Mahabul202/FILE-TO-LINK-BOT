import logging
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, BIN_CHANNEL
from web.server import web_server

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="FileToLinkBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins"),
            in_memory=True  # MANDATORY: Prevents the sqlite3 error on Cloudflare
        )

    async def start(self):
        await super().start()
        try:
            # Verify the bot can access the storage channel
            await self.get_chat(BIN_CHANNEL)
            print("✅ Connection to Bin Channel Verified")
        except Exception as e:
            print(f"❌ Bin Channel Error: {e}")

        # Start the web server for health checks
        self.runner = await web_server(self)
        print("✅ Web Server Started")

    async def stop(self, *args):
        await super().stop()
        # Clean up the web server on shutdown
        if hasattr(self, 'runner'):
            await self.runner.cleanup()
        print("🛑 Bot Stopped")
        
