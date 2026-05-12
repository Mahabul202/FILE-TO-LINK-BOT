# patch_pyrogram.py
import sys
from unittest.mock import MagicMock

# Mock sqlite3 before pyrogram imports it
sys.modules['sqlite3'] = MagicMock()
sys.modules['_sqlite3'] = MagicMock()
