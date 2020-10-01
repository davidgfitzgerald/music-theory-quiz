from unittest import TestCase
from note import Note


class TestNote(TestCase):
    def setUp(self):
        self.c = Note('c')
        self.c_sharp = Note('C#')
        self.d_flat = Note('Db')
        self.f = Note('F')
        self.f_sharp = Note('F#')
        self.b = Note('b')

    def test_name(self):
        self.assertEqual(self.c.name, "C")
        self.assertEqual(self.c_sharp.name, "C#")
        self.assertEqual(self.d_flat.name, "C#")
        self.assertEqual(self.b.name, "B")

    def test_next_note(self):
        self.assertEqual(self.c.next(), 'C#')
        self.assertEqual(self.b.next(), "C")

    def test_interval(self):
        self.assertEqual(self.b.interval_type(self.f_sharp), "Perfect 5th")
        self.assertEqual(self.c.interval_type(self.f), "Perfect 4th")
        self.assertEqual(self.c.interval_type(self.c), "Unison")
