import sys
import types

fake_sqlite3 = types.ModuleType("sqlite3")

class FakeConnection:
    def cursor(self): return FakeCursor()
    def commit(self): pass
    def close(self): pass
    def execute(self, *a, **kw): return FakeCursor()
    def __enter__(self): return self
    def __exit__(self, *a): pass

class FakeCursor:
    def execute(self, *a, **kw): pass
    def fetchone(self): return None
    def fetchall(self): return []
    def close(self): pass

fake_sqlite3.connect = lambda *a, **kw: FakeConnection()
fake_sqlite3.Connection = FakeConnection

sys.modules["sqlite3"] = fake_sqlite3
sys.modules["_sqlite3"] = fake_sqlite3
