import pygame
from MazeGenerator import Maze
import sys
from staffObject import StaffObject
from AudioFrequency import AudioFrequency

has_quit = False
def main():

	pygame.init()
	pygame.font.init()
	window_size = (1280,900)
	maze_pixel_size = (400,400)
	screen = pygame.display.set_mode((window_size[0], window_size[1]))

	# Set the pygame window name   
	pygame.display.set_caption('Music-Maze')

	background = pygame.image.load(r'img/textured-background.jpg')

	background = pygame.transform.scale(background, (window_size[0], window_size[1]))
	
	clock = pygame.time.Clock()
	screen.fill((255,255,255))

	SIZE_OF_GAME = (15,10)
	width = min(maze_pixel_size) / max(SIZE_OF_GAME)

	maze_offset = [(window_size[0]-maze_pixel_size[0])/2 , (window_size[1]-maze_pixel_size[1])/2]

	
	maze_o = Maze(screen, SIZE_OF_GAME, width, maze_offset)
	maze = maze_o.maze

	#Shared Audio Object
	audio = AudioFrequency()

	#Grand Staff Objects
	staffUp = StaffObject(screen, 550, 50)
	staffDown = StaffObject(screen, 550, 600)
	staffLeft = StaffObject(screen, 50, 300)
	staffRight = StaffObject(screen, 1050, 300)

	## END GAME DEBUGGING
	#maze_o.update_loc(14, 8)



	running = True
	global has_quit
	while running and not has_quit:
		screen.blit(background, (0, 0))
		for event in pygame.event.get():
			
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
					has_quit = True
					pygame.quit()
					sys.exit()

				#DEBUG - ALLOWS KEY PRESS MOVEMENT
				'''
				cx, cy = maze_o.current_loc
				#print(maze[cx][cy].north,maze[cx][cy].south,maze[cx][cy].west,maze[cx][cy].east)
				if event.key == pygame.K_UP:
					if not maze[cx][cy].south:
						#print('MOVE NORTH')
						maze_o.update_loc(cx, cy-1)
						staffUp.randomizeNote()
						staffDown.randomizeNote()
						staffLeft.randomizeNote()
						staffRight.randomizeNote()	
				if event.key == pygame.K_DOWN:
					if not maze[cx][cy].north:
						#print('MOVE SOUTH')

						maze_o.update_loc(cx, cy+1)

						staffUp.randomizeNote()
						staffDown.randomizeNote()
						staffLeft.randomizeNote()
						staffRight.randomizeNote()
				if event.key == pygame.K_LEFT:
					if not maze[cx][cy].west:
						maze_o.update_loc(cx-1, cy)
						staffUp.randomizeNote()
						staffDown.randomizeNote()
						staffLeft.randomizeNote()
						staffRight.randomizeNote()

				if event.key == pygame.K_RIGHT:	
					if not maze[cx][cy].east:
						maze_o.update_loc(cx+1, cy)
						staffUp.randomizeNote()
						staffDown.randomizeNote()
						staffLeft.randomizeNote()
						staffRight.randomizeNote()
				'''


			if event.type == pygame.QUIT:
				running = False
				has_quit = True
				pygame.quit()
				sys.exit()

		# Draws each of the maze rooms
		for i in range(SIZE_OF_GAME[1]):
			for j in range(SIZE_OF_GAME[0]):
				maze[j][i].draw()

		staffUp.reDraw()
		staffDown.reDraw()
		staffLeft.reDraw()
		staffRight.reDraw()
		
		notePlayed = audio.get_note()
		#print(notePlayed)
		isUp = staffUp.isNoteCorrect(notePlayed)
		isDown = staffDown.isNoteCorrect(notePlayed)
		isLeft = staffLeft.isNoteCorrect(notePlayed)
		isRight = staffRight.isNoteCorrect(notePlayed)

		cx, cy = maze_o.current_loc

		# If the end has been reached
		if maze[cx][cy].goal:
			running = False
			background = pygame.image.load(r'img/textured-background.jpg')
			background = pygame.transform.scale(background, (window_size[0], window_size[1]))
			screen.blit(background, (0, 0))
			myfont = pygame.font.SysFont('Comic Sans MS', 40)
			myfont2 = pygame.font.SysFont('Comic Sans MS', 20)
			textsurface = myfont.render('You Won!', True, (0, 0, 0))
			textsurface2 = myfont.render('Press any key to play again!', True, (0, 0, 0))
			textsurface3 = myfont2.render('or press the ESCAPE key to exit', True, (0, 0, 0))
			screen.blit(textsurface,(window_size[0]/2-85,window_size[1]/2-50))
			screen.blit(textsurface2,(window_size[0]/2-225,window_size[1]/2))
			screen.blit(textsurface3,(window_size[0]/2-125,window_size[1]/2+60))
			pygame.display.flip()

			while(1):
				for event in pygame.event.get():
							
					if event.type == pygame.QUIT:
						has_quit = True
						pygame.quit()
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							running = False
							has_quit = True
							pygame.quit()
							sys.exit()
						else:	
						# Restarts the game 
							return
			break
		if isUp:
			#Move up if possible
			if not maze[cx][cy].south:
				maze_o.update_loc(cx, cy-1)
				staffUp.randomizeNote()
				staffDown.randomizeNote()
				staffLeft.randomizeNote()
				staffRight.randomizeNote()
		elif isDown:
			#Move down if possible
			if not maze[cx][cy].north:
				#print('MOVE SOUTH')
				maze_o.update_loc(cx, cy+1)
				staffUp.randomizeNote()
				staffDown.randomizeNote()
				staffLeft.randomizeNote()
				staffRight.randomizeNote()
		elif isLeft:
			#Move left if possible
			if not maze[cx][cy].west:
				maze_o.update_loc(cx-1, cy)
				staffUp.randomizeNote()
				staffDown.randomizeNote()
				staffLeft.randomizeNote()
				staffRight.randomizeNote()
		elif isRight:
			#Move right if possible
			if not maze[cx][cy].east:
				maze_o.update_loc(cx+1, cy)
				staffUp.randomizeNote()
				staffDown.randomizeNote()
				staffLeft.randomizeNote()
				staffRight.randomizeNote()

		pygame.display.flip()
		clock.tick(30)

	has_quit = True
	pygame.quit()
	sys.exit




if (__name__ == "__main__"):
	while not has_quit:
		main()
