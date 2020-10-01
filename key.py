class Key(object):
    def __init__(self, rootnote, scale="Major"):
        self.rootnote = rootnote
        self.scale = scale
        self.notes = self.get_notes

    def get_notes(self):
        return
