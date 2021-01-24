import pygame
from MazeGenerator import Maze
import sys


def main():
	pygame.init()
	window_size = (1000,1000)
	screen = pygame.display.set_mode((window_size[0], window_size[1]))
	#screen.fill((255,255,255))
	clock = pygame.time.Clock()
	screen.fill((255,255,255))

	SIZE_OF_GAME = (15,10)
	width = min(window_size) / max(SIZE_OF_GAME)

	#print(width)
	maze_o = Maze(screen, SIZE_OF_GAME, width)
	maze = maze_o.maze
	maze_o.update_loc(1,2)
	#print(maze)
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		
		for i in range(SIZE_OF_GAME[1]):
			for j in range(SIZE_OF_GAME[0]):
				
				
				maze[j][i].draw()

		pygame.display.flip()
		clock.tick(30)

	pygame.quit()
	sys.exit

main()
