import random as rand
import copy

def make_2D_array(rows, cols):
	"""
	Creates an empty two dimensional array

    Args: 
    rows: the number of rows in the array
    cols: the number of columns in the array

    Returns:
    make_2D_array(2,2): [ [[], []], 
                          [[], []] ]
	"""
	array = []
	for i in range(rows):
		array.append([])
		for j in range(cols):
			array[i].append([])
	return array 


def Grid(grid):
	"""
	Creates a grid filled with zeros and ones from an empty array
	zero represents a dead cell and one represents a dead cell

	Args:
	    grid: a two dimensional array

	Returns:
	    Grid(make_2D_array(2,2)): [ [[0], [1]], 
                                    [[1], [0]] ]
	"""
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			grid[i][j] = rand.randint(0,1)
	return grid


def logic(grid):
	"""
	Applies the rules of 'Conway's Game of Life' which can be found
	on the following link: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

	Args:
	    grid: two dimensional array filled with zeros and ones which the rules
	           of the game will be applied to.

	Returns:
	    logic(grid): a new grid in which the rules of the game have been applied
	                 to a previously existing grid
	"""
	next_grid = copy.deepcopy(grid)
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			state = grid[i][j]
			total = 0
			neighbours = count_neighbours(grid, i, j)
			if state == 0 and neighbours == 3:
				next_grid[i][j] = 1
			elif state == 1 and neighbours < 2 or neighbours > 3:
				next_grid[i][j] = 0
			else:
				next_grid[i][j] == grid[i][j]
	return next_grid


def count_neighbours(grid, x , y):
	"""
	Checks all eight nearest numbers of a given cell and sums up their value.
	If cell is at the edge of the grid, any point which is checked that falls
	outside the grid is reflected to the other side of the grid to give an
	infinite dimensional universe - (wrap around world)

	Args:
	    grid: two dimensional grid of zeros and ones
	    x: row position on grid
	    y: column position on grid

	Returns: 
	    count_nieghbours(grid,x,y): the sum of all the values of the nearest neighbours

	"""
	total = 0
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			mod_rows = (x + i + len(grid)) % len(grid)
			mod_cols = (y + j + len(grid[i])) % len(grid[i])
			total += grid[mod_rows][mod_cols] 		
	total -= grid[x][y]
	return total
