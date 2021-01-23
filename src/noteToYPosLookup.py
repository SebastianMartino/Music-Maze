class NoteToYPosLookup:

    def __init__(self, F5, E4, C4, A3, G2):
        self.trebHeight = (E4 - F5)
        self.bassHeight = (G2 - A3)

        self.moveSpaceTreb = self.trebHeight // 8
        self.moveSpaceBass = self.bassHeight // 8

        self.lookupTable = {
            "F5": F5,
            "F#5/Gb5": F5,

            "E5": F5 + self.moveSpaceTreb,
            "E#5/F5": F5 + self.moveSpaceTreb,

            "D5": F5 + (2*self.moveSpaceTreb),
            "D#5/Eb5": F5 + (2*self.moveSpaceTreb),

            "C5": F5 + (3*self.moveSpaceTreb),
            "C#5/Db5": F5 + (3*self.moveSpaceTreb),

            "B4": F5 + (4*self.moveSpaceTreb),
            "B#4/C5": F5 + (4*self.moveSpaceTreb),

            "A4": F5 + (5*self.moveSpaceTreb),
            "A#4/Bb4": F5 + (5*self.moveSpaceTreb),

            "G4": F5 + (6*self.moveSpaceTreb),
            "G#4/Ab4": F5 + (6*self.moveSpaceTreb),

            "F4": F5 + (7*self.moveSpaceTreb),
            "F#4/Gb4": F5 + (7*self.moveSpaceTreb),

            "E4": E4,
            "E#4/F4": E4,

            "D4": E4 + self.moveSpaceTreb,
            "D#4/Eb4": E4 + self.moveSpaceTreb,

            "C4": C4,
            "C#4/Db4": C4,

            "B3": A3 - self.moveSpaceBass,
            "B#3/C4": A3 - self.moveSpaceBass,

            "A3": A3,
            "A#3/Bb3": A3,

            "G3": A3 + self.moveSpaceBass,
            "G#3/Ab3": A3 + self.moveSpaceBass,

            "F3": A3 + (2*self.moveSpaceBass),
            "F#3/Gb4": A3 + (2*self.moveSpaceBass),

            "E3": A3 + (3*self.moveSpaceBass),
            "E#3/F3": A3 + (3*self.moveSpaceBass),

            "D3": A3 + (4*self.moveSpaceBass),
            "D#3/Eb3": A3 + (4*self.moveSpaceBass),

            "C3": A3 + (5*self.moveSpaceBass),
            "C#3/Db3": A3 + (5*self.moveSpaceBass),

            "B2": A3 + (6*self.moveSpaceBass),
            "B#2/C3": A3 + (6*self.moveSpaceBass),

            "A2": A3 + (7*self.moveSpaceBass),
            "A#2/Bb2": A3 + (7*self.moveSpaceBass),

            "G2": G2,
            "G#2/Ab2": G2

        }

    def lookupYPos(self, noteDescription):
        return self.lookupTable.get(noteDescription, None)

