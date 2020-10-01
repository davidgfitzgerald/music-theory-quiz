from unittest import TestCase

from chord import Chord
from note import Note


class TestChord(TestCase):
    def setUp(self):
        self.c = Note("c")
        self.c_sharp = Note("c#")
        self.d_sharp = Note("d#")
        self.e = Note("e")
        self.f = Note("f")
        self.f_sharp = Note("f#")
        self.g = Note("g")
        self.g_sharp = Note("g#")
        self.b = Note("b")
        self.b_flat = Note("Bb")
        self.c_major = Chord([self.c, self.e, self.g])
        self.c_major7th = Chord([self.c, self.e, self.g, self.b])

        self.c_dominant7th = Chord([self.c, self.e, self.g, self.b_flat])
        self.c_altered1 = Chord([self.c, self.c_sharp, self.e, self.b_flat])
        self.c_altered2 = Chord([self.c, self.d_sharp, self.e, self.b_flat])
        self.c_altered3 = Chord([self.c, self.e, self.f_sharp, self.b_flat])
        self.c_altered4 = Chord([self.c, self.e, self.g_sharp, self.b_flat])

    def test_qualities(self):
        self.assertEqual(self.c_major.qualities, ["Major 3rd", "Perfect 5th"])

    def test_name(self):
        self.assertEqual(self.c_major.__str__(), "C Major")

    def test_major_chord(self):
        self.assertEqual(self.c_major.description, 'Major')

    def test_major7th_chord(self):
        self.assertEqual(self.c_major7th.description, "Major 7th")

    def test_dominant7th_chord(self):
        self.assertEqual(self.c_dominant7th.description, "Dominant 7th")

    def test_altered_chord(self):
        self.assertEqual(self.c_altered1.description, "Altered")
        self.assertEqual(self.c_altered2.description, "Altered")
        self.assertEqual(self.c_altered3.description, "Altered")
        self.assertEqual(self.c_altered4.description, "Altered")


