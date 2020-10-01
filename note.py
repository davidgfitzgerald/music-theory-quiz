from config import NOTES, INTERVALS


class Note(object):
    def __init__(self, name):
        self.enharmonic = None
        self.name = self.parse_name(name)

    def parse_name(self, name):
        if len(name) == 1:
            return name.upper()
        elif len(name) == 2:
            if name[1].lower() == 'b':
                self.enharmonic = name[0].upper() + name[1]
                return NOTES[NOTES.index(name[0])-1]
            elif name[1] == "#":
                self.enharmonic = NOTES[NOTES.index(name)+1]+"b"
                return name[0].upper() + name[1]
        else:
            raise ValueError("Length of note name longer than two")

    def __str__(self):
        return str(self.name)

    def next(self):  # The next chromatic note
        q, r = divmod(NOTES.index(self.name)+1, 12)
        return NOTES[r]

    def prev(self):  # The previous chromatic note
        q, r = divmod(NOTES.index(self.name)-1, 12)
        return NOTES[r]

    def up(self, semitones):  # The note up this many semitones
        q, r = divmod(NOTES.index(self.name) + semitones, 12)
        return NOTES[r]

    def interval_type(self, higher_note):  # The interval type e.g: Major 3rd
        semitones = (NOTES.index(higher_note.name) - NOTES.index(self.name)) % 12
        return INTERVALS[semitones]
