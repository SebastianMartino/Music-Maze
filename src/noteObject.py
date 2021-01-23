# Note Object Class

class NoteObject:

    def __init__(self):

        self.noteDescription = "F5"

        self.xPos = 0

        self.yPos = 0

        self.size = 20

    def setXPos(self, newXPos):
        self.xPos = newXPos

    def setYPos(self, newYPos):
        self.yPos = newYPos

    def setSize(self, newSize):
        self.size = newSize

    def setNote(self, newNoteDescription):
        self.noteDescription = newNoteDescription