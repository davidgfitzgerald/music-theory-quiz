class Chord(object):
    def __init__(self, notes):
        self.notes = notes
        self.qualities = self.set_qualities()
        self.description = self.set_desc()

    def __str__(self):
        return f"{self.notes[0]} {self.description}"

    def set_qualities(self):
        return [self.notes[0].interval_type(higher) for higher in self.notes[1:]]

    def set_desc(self):  # Description of the chord
        if "Major 3rd" in self.qualities:
            if "Minor 7th" in self.qualities:
                if "Minor 2nd" in self.qualities or "Minor 3rd" in self.qualities or \
                        "Flat 5th" in self.qualities or "Minor 6th" in self.qualities:
                    return "Altered"
                return "Dominant 7th"
            if "Major 7th" in self.qualities:
                return "Major 7th"
            if "Perfect 5th" in self.qualities:
                return "Major"
        if "Minor 3rd" in self.qualities:
            if "Minor 7th" in self.qualities:
                return "Minor 7th"
            if "Major 7th" in self.qualities:
                return "Minor-Major 7th"
            if "Perfect 5th" in self.qualities:
                return "Minor"
