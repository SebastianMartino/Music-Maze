import pygame
from MazeGenerator import Maze
import sys


def main():
	pygame.init()
	window_size = (1500,1000)
	maze_pixel_size = (500,500)
	screen = pygame.display.set_mode((window_size[0], window_size[1]))
	#screen.fill((255,255,255))
	clock = pygame.time.Clock()
	screen.fill((255,255,255))

	SIZE_OF_GAME = (15,10)
	width = min(maze_pixel_size) / max(SIZE_OF_GAME)

	maze_offset = [(window_size[0]-maze_pixel_size[0])/2 , (window_size[1]-maze_pixel_size[1])/2]

	#print(width)
	maze_o = Maze(screen, SIZE_OF_GAME, width, maze_offset)
	maze = maze_o.maze


	maze_o.update_loc(1,2)

	x,y = maze_o.current_loc
	maze[x][y].north
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
