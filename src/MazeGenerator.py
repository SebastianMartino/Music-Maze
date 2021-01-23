import random
from enum import Enum
class Maze:
	class Room:
		def __init__(self, x, y):
			self.x = x
			self.y = y

			#True means there IS a wall in direction, False = no wall
			self.north = None
			self.east = None
			self.west = None
			self.south = None

			self.visisted = False
			
	class Dir(Enum):
		NORTH = 0
		EAST = 1
		WEST = 2
		SOUTH = 3

	def __init__(self, size, start_loc, end_loc):
		self.maze = []
		self.size = size
		for i in range(size[0]):
			temp = []
			for j in range(size[1]):
				temp.append(self.Room(i, j))
			self.maze.append(temp)
		self.drunken_walk(0,0)	
		print(self.maze)
		self.print_maze()

	def get_offset(self, direction):
		if direction == self.Dir.NORTH:
			return [0, 1]
		elif direction == self.Dir.EAST:
			return [1, 0]
		elif direction == self.Dir.WEST:
			return [-1, 0]
		elif direction == self.Dir.SOUTH:
			return [0, -1]

	def check_bounds(self, row, col):
		if row >= self.size[0] or row < 0:
			return False
		elif col >= self.size[1] or col < 0:
			return False
		return True
	
	def check_wall(self, room, direction):
		if direction == self.Dir.NORTH:
			return room.north
		elif direction == self.Dir.EAST:
			return room.east
		elif direction == self.Dir.WEST:
			return room.west
		elif direction == self.Dir.SOUTH:
			return room.south

	def opposite_dir(self, direction):
		if direction == self.Dir.NORTH:
			return self.Dir.SOUTH
		elif direction == self.Dir.EAST:
			return self.Dir.WEST
		elif direction == self.Dir.WEST:
			return self.Dir.EAST
		elif direction == self.Dir.SOUTH:
			return self.Dir.NORTH

	def set_room_dir(self, room, direction, wall):
		if wall == True:
			if direction == self.Dir.NORTH:
				room.north = True
			elif direction == self.Dir.EAST:
				room.east = True
			elif direction == self.Dir.WEST:
				room.west = True
			elif direction == self.Dir.SOUTH:
				room.south = True
		else:
			if direction == self.Dir.NORTH:
				room.north = False
			elif direction == self.Dir.EAST:
				room.east = False
			elif direction == self.Dir.WEST:
				room.west = False
			elif direction == self.Dir.SOUTH:
				room.south = False

	def print_maze(self):
		for x in range(self.size[0]):
			for y in range(self.size[1]):\
			print(self.maze[x][y].north,self.maze[x][y].east,self.maze[x][y].west,self.maze[x][y].south)

	def drunken_walk(self, row, col):
		room = self.maze[row][col]
		room.visisted = True
		directions = [self.Dir.NORTH, self.Dir.EAST, self.Dir.WEST, self.Dir.SOUTH]
		random.shuffle(directions)
		for direction in directions:
			offset = self.get_offset(direction)
			if self.check_bounds(row+offset[0], col+offset[1]) == False:
				self.set_room_dir(room, direction, wall=True)
			else:
				neighbor = self.maze[row+offset[0]][col+offset[1]]
				if neighbor.visisted == False:
					self.set_room_dir(room, direction, wall=False)
					self.drunken_walk(neighbor.x, neighbor.y)
				else:
					opp_dir = self.opposite_dir(direction)
					wall_val = self.check_wall(neighbor, opp_dir)
					if wall_val != None:
						self.set_room_dir(room, direction, wall_val)
					else:
						self.set_room_dir(room, direction, wall=True)









	

	

Maze((10,10), 0, 0)