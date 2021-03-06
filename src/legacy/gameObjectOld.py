# Imports
import pygame
from pygame.locals import *
import sys
import noteObject
import noteToYPosLookup
from AudioFrequency import AudioFrequency
import random

# pygame GameObject class
class GameObject:

    # RGB Color Definitions
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)

    # Assigning val for height and width of screen (720p)
    screenHeight = 720  
    screenWidth = 1280

    # Assigning val for height and width of staff image
    staffHeight = 720
    staffWidth = 1280

    def __init__ (self):

        # Initialize pygame
        pygame.init()
        # Create AudioFrequency Object for note recognition
        self.audio = AudioFrequency()
        # Assign FPS value
        self.FPS = 30
        self.FramePerSec = pygame.time.Clock()

        # Creating the display surface  
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.background = pygame.image.load(r'../img/textured-background.jpg')
        

        # Set the pygame window name   
        pygame.display.set_caption('Music-Maze')

        # Create surface object with staff image drawn on it 
        self.staffImage = pygame.image.load(r'../img/grandStaff.png')
        self.staffImage = pygame.transform.scale(self.staffImage, (self.staffWidth, self.staffHeight - 50)) 

        # Blit image onto screen
        self.screen.blit(self.background, (0, 0))     
        self.screen.blit(self.staffImage, (0, 0))

        # Create lookup table for note y coordinates
        self.noteYLookup = noteToYPosLookup.NoteToYPosLookup(60,246,361,480,666)

        # Create first note on F5
        self.note1 = noteObject.NoteObject()
        self.updateNote(self.note1, "E#5/F5")



    # Function to move a note on the screen
    def updateNote(self, noteInst, noteDescription):

        #Use lookup table to find y pos of note
        newYpos = self.noteYLookup.lookupYPos(noteDescription)

        if newYpos != None:
            # Fill Screen & Re-Blit the staff
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.staffImage, (0, 0))

            # Update internal note parameters
            noteInst.setNote(noteDescription)
            noteInst.setXPos(500)
            noteInst.setYPos(newYpos)

            noteSprite = pygame.image.load(r'../img/quarter-note.png').convert_alpha()

            # pygame.draw.circle(self.screen, self.BLACK, (noteInst.xPos, noteInst.yPos), noteInst.size)
            # pygame.draw.line(self.screen,self.BLACK,(noteInst.xPos + (noteInst.size - 5),noteInst.yPos),(noteInst.xPos + (noteInst.size - 5),noteInst.yPos - 80), 7)

            #Check if note is a sharp
            if("#" in noteDescription):
                # pygame.draw.line(self.screen, self.BLACK, (noteInst.xPos + (noteInst.size +5), noteInst.yPos - 10), (noteInst.xPos + (noteInst.size + 20), noteInst.yPos - 10), 3)
                # pygame.draw.line(self.screen, self.BLACK, (noteInst.xPos + (noteInst.size + 12.5), noteInst.yPos - 20), (noteInst.xPos + (noteInst.size + 12.5), noteInst.yPos), 3)
                noteSprite = pygame.image.load(r'../img/quarter-note-sharp.png').convert_alpha()
            
            #Check if note is middle c
            if("C4" in noteDescription or "C#4" in noteDescription):
                pygame.draw.line(self.screen, self.BLACK, (noteInst.xPos, noteInst.yPos), (noteInst.xPos + (noteInst.width), noteInst.yPos), 7)
                # noteSprite = pygame.image.load("quarter-note-sharp.png").convert_alpha()
            
            noteSprite = pygame.transform.scale(noteSprite, (noteInst.width, noteInst.height))
            self.screen.blit(noteSprite, (noteInst.xPos, noteInst.yPos - noteInst.height + (noteInst.height/6)))

    # Helper function to check for correct note played
    def isNoteCorrect(self):
        notePlayed = self.audio.get_note()
        if notePlayed in self.note1.noteDescription:
            return True
        else:
            return False


    # Boiler plate code for every game loop
    def gameLoopBoilerPlate(self):
        # Update Screen   
        pygame.display.flip()
   
        #Check for events
        for event in pygame.event.get():
            # Check for quit event & close program  
            if event.type == QUIT:  
                pygame.quit()
                self.audio.close()
                sys.exit()
                # quit the program.   
                quit()
        self.FramePerSec.tick(self.FPS)



    # Main game loop (listen mode)
    def gameLoopInstanceListenMode(self):
        self.gameLoopBoilerPlate()
        # Update note position based on tone recognized by microphone
        self.updateNote(self.note1, self.audio.get_note())



    # Main game loop (play mode)
    def gameLoopInstancePlayMode(self):
        self.gameLoopBoilerPlate()
        if(self.isNoteCorrect()):
            newNote = random.choice(list(self.noteYLookup.lookupTable.keys()))
            self.updateNote(self.note1, newNote)
        return self.isNoteCorrect()

