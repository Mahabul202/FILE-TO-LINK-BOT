import sys
from unittest.mock import MagicMock

# Mock sqlite3 BEFORE any pyrogram imports
# Pyrogram imports it at module level even when using in_memory=True
sys.modules["sqlite3"] = MagicMock()
sys.modules["_sqlite3"] = MagicMock()  # also mock the C extension directly

import asyncio
from bot import Bot

async def main():
    bot = Bot()
    await bot.start()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())

#gsgs
