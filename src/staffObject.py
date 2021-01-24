# Imports
import pygame
from pygame.locals import *
import sys
import noteObject
import noteToYPosLookup
from AudioFrequency import AudioFrequency
import random

# pygame StaffObject class
class StaffObject:

    # Assigning val for height and width of staff image
    staffHeight = 250
    staffWidth = 350

    BLACK = (0,0,0)

    def __init__ (self, screen, staffX, staffY):

        self.screen = screen

        self.staffX = staffX

        self.staffY = staffY

        self.noteXOffset = staffX + 100
       
        # Create AudioFrequency Object for note recognition
        self.audio = AudioFrequency()


        # Create surface object with staff image drawn on it 
        self.staffImage = pygame.image.load(r'img/grandStaff.png')
        self.staffImage = pygame.transform.scale(self.staffImage, (self.staffWidth, self.staffHeight)) 

        # Blit image onto screen   
        self.screen.blit(self.staffImage, (staffX, staffY))

        # Create lookup table for note y coordinates
        self.noteYLookup = noteToYPosLookup.NoteToYPosLookup(staffY + 21 , staffY + 95, staffY + 135, staffY + 179, staffY + 252)

        # Create first random note
        self.note = noteObject.NoteObject()
        newNote = random.choice(list(self.noteYLookup.lookupTable.keys()))
        self.updateNote(self.note, newNote)
        # Manual Note Debugging
        # self.updateNote(self.note, "G2")


    def reDraw(self):
        self.screen.blit(self.staffImage, (self.staffX, self.staffY))
        self.updateNote(self.note, self.note.noteDescription)

    # Function to move a note on the screen
    def updateNote(self, noteInst, noteDescription):

        #Use lookup table to find y pos of note
        newYpos = self.noteYLookup.lookupYPos(noteDescription)

        if newYpos != None:
            # Re-Blit the staff
            self.screen.blit(self.staffImage, (self.staffX, self.staffY))

            # Update internal note parameters
            noteInst.setNote(noteDescription)
            noteInst.setXPos(self.noteXOffset)
            noteInst.setYPos(newYpos)

            noteSprite = pygame.image.load(r'img/quarter-note.png').convert_alpha()

            # pygame.draw.circle(self.screen, self.BLACK, (noteInst.xPos, noteInst.yPos), noteInst.size)
            # pygame.draw.line(self.screen,self.BLACK,(noteInst.xPos + (noteInst.size - 5),noteInst.yPos),(noteInst.xPos + (noteInst.size - 5),noteInst.yPos - 80), 7)

            #Check if note is a sharp
            if("#" in noteDescription):
                # pygame.draw.line(self.screen, self.BLACK, (noteInst.xPos + (noteInst.size +5), noteInst.yPos - 10), (noteInst.xPos + (noteInst.size + 20), noteInst.yPos - 10), 3)
                # pygame.draw.line(self.screen, self.BLACK, (noteInst.xPos + (noteInst.size + 12.5), noteInst.yPos - 20), (noteInst.xPos + (noteInst.size + 12.5), noteInst.yPos), 3)
                noteSprite = pygame.image.load(r'img/quarter-note-sharp.png').convert_alpha()
            
            #Check if note is middle c
            # if("C4" in noteDescription or "C#4" in noteDescription):
            #     pygame.draw.line(self.screen, self.BLACK, (noteInst.xPos, noteInst.yPos), (noteInst.xPos + (noteInst.width), noteInst.yPos), 7)
            #     # noteSprite = pygame.image.load("quarter-note-sharp.png").convert_alpha()
            
            noteSprite = pygame.transform.scale(noteSprite, (noteInst.width, noteInst.height))
            self.screen.blit(noteSprite, (noteInst.xPos, noteInst.yPos - noteInst.height + (noteInst.height/6)))

    # Helper function to check for correct note played
    def isNoteCorrect(self, notePlayed):
        if notePlayed in self.note.noteDescription:
            return True
        else:
            return False



    # Main game loop (play mode)
    def randomizeNote(self):
        newNote = random.choice(list(self.noteYLookup.lookupTable.keys()))
        self.updateNote(self.note, newNote)


