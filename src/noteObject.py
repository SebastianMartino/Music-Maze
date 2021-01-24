# Note Object Class

class NoteObject:

    def __init__(self):

        self.noteDescription = "F5"

        self.xPos = 0

        self.yPos = 0

        self.height = 75

        self.width = 50

    def setXPos(self, newXPos):
        self.xPos = newXPos

    def setYPos(self, newYPos):
        self.yPos = newYPos

    def setHeight(self, newHeight):
        self.height = newHeight

    def setWidth(self, newWidth):
        self.width = newWidth

    def setNote(self, newNoteDescription):
        self.noteDescription = newNoteDescription
