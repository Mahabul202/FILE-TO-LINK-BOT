import sys
from unittest.mock import MagicMock

# THIS MUST COME BEFORE 'from bot import Bot'
# It tricks the system into thinking sqlite3 is there
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
    
