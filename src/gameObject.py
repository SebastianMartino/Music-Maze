# Imports
import pygame
from pygame.locals import *
import sys
import noteObject

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

        self.note = noteObject.NoteObject()
        self.note.setXPos(500)
        self.note.setYPos(0)

        pygame.draw.circle(self.screen, self.BLACK, (self.note.xPos, self.note.yPos), self.note.size)


    # Function to move a note on the screen
    def moveNote(self, noteInst, newX, newY):

        # Check that note isn't moving off of screen
        if (newX > 0 and newX < self.staffWidth and newY > 0 and newY < self.staffHeight):
            # Fill Screen & Re-Blit the staff
            self.screen.fill(self.WHITE)
            self.screen.blit(self.staffImage, (0, 0))

            noteInst.setXPos(newX)
            print("X Position: " + str(newX))

            noteInst.setYPos(newY)
            print("Y Position: " + str(newY))

            pygame.draw.circle(self.screen, self.BLACK, (noteInst.xPos, noteInst.yPos), noteInst.size)


    # Main game loop
    def gameLoopInstance(self):

        # Update Screen   
        pygame.display.update()
   
        #Check for events
        for event in pygame.event.get():
            # Check for quit event & close program  
            if event.type == QUIT:  
                pygame.quit()
                sys.exit()
                # quit the program.   
                quit()
            #Check for key press events
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.moveNote(self.note, 500, self.note.yPos + 1)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.moveNote(self.note, 500, self.note.yPos - 1)

        self.FramePerSec.tick(self.FPS)


