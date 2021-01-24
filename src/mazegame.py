import pygame
from MazeGenerator import Maze
import sys
from staffObject import StaffObject
from AudioFrequency import AudioFrequency


def main():
	pygame.init()
	window_size = (1280,900)
	maze_pixel_size = (400,400)
	screen = pygame.display.set_mode((window_size[0], window_size[1]))

	# Set the pygame window name   
	pygame.display.set_caption('Music-Maze')

	background = pygame.image.load(r'../img/textured-background.jpg')

	background = pygame.transform.scale(background, (window_size[0], window_size[1]))
	#screen.fill((255,255,255))
	clock = pygame.time.Clock()
	screen.fill((255,255,255))

	SIZE_OF_GAME = (15,10)
	width = min(maze_pixel_size) / max(SIZE_OF_GAME)

	maze_offset = [(window_size[0]-maze_pixel_size[0])/2 , (window_size[1]-maze_pixel_size[1])/2]

	#print(width)
	maze_o = Maze(screen, SIZE_OF_GAME, width, maze_offset)
	maze = maze_o.maze


	#maze_o.update_loc(1,2)

	#x,y = maze_o.current_loc
	#maze[x][y].north
	#print(maze)

	#Shared Audio Object
	audio = AudioFrequency()

	#Grand Staff Objects
	staffUp = StaffObject(screen, 550, 50)
	staffDown = StaffObject(screen, 550, 600)
	staffLeft = StaffObject(screen, 50, 300)
	staffRight = StaffObject(screen, 1050, 300)


	running = True
	while running:
		screen.blit(background, (0, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		
		for i in range(SIZE_OF_GAME[1]):
			for j in range(SIZE_OF_GAME[0]):
				
				
				maze[j][i].draw()

		staffUp.reDraw()
		staffDown.reDraw()
		staffLeft.reDraw()
		staffRight.reDraw()
		
		notePlayed = audio.get_note()
		isUp = staffUp.isNoteCorrect(notePlayed)
		isDown = staffDown.isNoteCorrect(notePlayed)
		isLeft = staffLeft.isNoteCorrect(notePlayed)
		isRight = staffRight.isNoteCorrect(notePlayed)

		cy, cx = maze_o.current_loc
		if isUp:
			#Move up if possible
			if maze[cx][cy].north:
				maze_o.update_loc(cy+1, cx)
				staffUp.randomizeNote()
				staffDown.randomizeNote()
				staffLeft.randomizeNote()
				staffRight.randomizeNote()
		elif isDown:
			#Move down if possible
			if maze[cx][cy].south:
				maze_o.update_loc(cy-1, cx)
				staffUp.randomizeNote()
				staffDown.randomizeNote()
				staffLeft.randomizeNote()
				staffRight.randomizeNote()
		elif isLeft:
			#Move left if possible
			if maze[cx][cy].west:
				maze_o.update_loc(cy, cx-1)
				staffUp.randomizeNote()
				staffDown.randomizeNote()
				staffLeft.randomizeNote()
				staffRight.randomizeNote()
		elif isRight:
			#Move right if possible
			if maze[cx][cy].east:
				maze_o.update_loc(cy, cx+1)
				staffUp.randomizeNote()
				staffDown.randomizeNote()
				staffLeft.randomizeNote()
				staffRight.randomizeNote()

		pygame.display.flip()
		clock.tick(30)

	pygame.quit()
	sys.exit

if (__name__ == "__main__"):
    main()
