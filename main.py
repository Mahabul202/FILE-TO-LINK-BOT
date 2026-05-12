import sys
from unittest.mock import MagicMock

# Mock sqlite3 to bypass the missing module error on Cloudflare
mock_sqlite3 = MagicMock()
sys.modules["sqlite3"] = mock_sqlite3

import asyncio
from bot import Bot

async def main():
    bot = Bot()
    await bot.start()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
    
