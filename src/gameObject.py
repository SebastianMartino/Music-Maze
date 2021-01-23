# Imports
import pygame
from pygame.locals import *
import sys
import noteObject
import noteToYPosLookup
from AudioFrequency import AudioFrequency

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
        self.audio = AudioFrequency()
        # Assign FPS value
        self.FPS = 30
        self.FramePerSec = pygame.time.Clock()

        # Creating the display surface  
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.screen.fill(self.WHITE)

        # Set the pygame window name   
        pygame.display.set_caption('Music-Maze')

        # Create surface object with staff image drawn on it 
        self.staffImage = pygame.image.load(r'../img/grandStaff.png')
        self.staffImage = pygame.transform.scale(self.staffImage, (self.staffWidth, self.staffHeight - 50)) 

        # Blit image onto screen     
        self.screen.blit(self.staffImage, (0, 0))

        # Create lookup table for note y coordinates
        self.noteYLookup = noteToYPosLookup.NoteToYPosLookup(60,246,361,480,666)

        # Create first note on F5
        self.note1 = noteObject.NoteObject()
        self.note1.setXPos(500)
        self.note1.setYPos(60)

        pygame.draw.circle(self.screen, self.BLACK, (self.note1.xPos, self.note1.yPos), self.note1.size)


    # Function to move a note on the screen
    def updateNote(self, noteInst, noteDescription):

        #Use lookup table to find y pos of note
        newYpos = self.noteYLookup.lookupYPos(noteDescription)

        if newYpos != None:
            # Fill Screen & Re-Blit the staff
            self.screen.fill(self.WHITE)
            self.screen.blit(self.staffImage, (0, 0))

            # Update internal note parameters
            noteInst.setNote(noteDescription)
            noteInst.setXPos(500)
            noteInst.setYPos(newYpos)

            pygame.draw.circle(self.screen, self.BLACK, (noteInst.xPos, noteInst.yPos), noteInst.size)
            pygame.draw.line(self.screen,self.BLACK,(noteInst.xPos + (noteInst.size - 5),noteInst.yPos),(noteInst.xPos + (noteInst.size - 5),noteInst.yPos - 80), 7)

            #Check if note is a sharp
            if("#" in noteDescription):
                pygame.draw.line(self.screen, self.BLACK, (noteInst.xPos + (noteInst.size +5), noteInst.yPos - 10), (noteInst.xPos + (noteInst.size + 20), noteInst.yPos - 10), 3)
                pygame.draw.line(self.screen, self.BLACK, (noteInst.xPos + (noteInst.size + 12.5), noteInst.yPos - 20), (noteInst.xPos + (noteInst.size + 12.5), noteInst.yPos), 3)
            
            #Check if note is middle c
            if("C4" in noteDescription or "C#4" in noteDescription):
                pygame.draw.line(self.screen, self.BLACK, (noteInst.xPos - (noteInst.size + 20), noteInst.yPos), (noteInst.xPos + (noteInst.size + 20), noteInst.yPos), 7)
            


    # Main game loop
    def gameLoopInstance(self):

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
            if event.type == pygame.KEYDOWN and event.key ==pygame.K_g:
                self.updateNote(self.note1, "G4")
            if event.type == pygame.KEYDOWN and event.key ==pygame.K_b:
                self.updateNote(self.note1, "B4")
            if event.type == pygame.KEYDOWN and event.key ==pygame.K_d:
                self.updateNote(self.note1, "D3")
            if event.type == pygame.KEYDOWN and event.key ==pygame.K_a:
                self.updateNote(self.note1, "A3")

        self.updateNote(self.note1, self.audio.get_note())
        

        self.FramePerSec.tick(self.FPS)


