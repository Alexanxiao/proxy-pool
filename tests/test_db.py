from core.db import DBManager
import unittest

class TestDB(unittest.TestCase):
    def setUp(self):
        self.conn = DBManager()

    def test_get(self):
        print(self.conn.get())

    def test_pop(self):
        print(self.conn.pop())

    def test_size(self):
        print(self.conn.size)

    def test_flush(self):
        self.conn.flush()
        print(self.conn.size)

if __name__ == '__main__':
    unittest.main()