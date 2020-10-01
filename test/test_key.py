from unittest import TestCase
from key import Key


class TestKey(TestCase):
    def setUp(self):
        self.C = Key("C")

    def test_cmajor(self):
        self.assertEqual(self.C.notes(), ["C", "D", "E", "F", "G", "A", "B"])
