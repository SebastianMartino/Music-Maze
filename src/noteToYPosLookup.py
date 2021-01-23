class NoteToYPosLookup:

    def __init__(self, F5, E4, C4, A4, G2):
        self.trebHeight = (E4 - F5)
        self.bassHeight = (G2 - A4)

        self.moveSpaceTreb = self.trebHeight // 8
        self.moveSpaceBass = self.bassHeight // 8

        self.lookupTable = {
            "F5": F5,
            "E5": F5 + self.moveSpaceTreb,
            "D5": F5 + (2*self.moveSpaceTreb),
            "C5": F5 + (3*self.moveSpaceTreb),
            "B5": F5 + (4*self.moveSpaceTreb),
            "A5": F5 + (5*self.moveSpaceTreb),
            "G4": F5 + (6*self.moveSpaceTreb),
            "F4": F5 + (7*self.moveSpaceTreb),
            "F4": F5 + (8*self.moveSpaceTreb),
            "E4": E4,
            "D4": E4 + self.moveSpaceTreb,
            "C4": C4,
            "B4": A4 - self.moveSpaceBass,
            "A4": A4,
            "G3": A4 + self.moveSpaceBass,
            "F3": A4 + (2*self.moveSpaceBass),
            "E3": A4 + (3*self.moveSpaceBass),
            "D3": A4 + (4*self.moveSpaceBass),
            "C3": A4 + (5*self.moveSpaceBass),
            "B3": A4 + (6*self.moveSpaceBass),
            "A3": A4 + (7*self.moveSpaceBass),
            "G2": G2

        }

    def lookupYPos(self, noteDescription):
        return self.lookupTable.get(noteDescription, None)

