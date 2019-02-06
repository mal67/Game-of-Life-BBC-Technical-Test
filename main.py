"""
Title: Conway's Game of Life

Author: Mohamed A. Laleg
For: BBC

Assumptions: 
           1. Cells outside of grid will be reflected to opossite side of grid (Wrap Around World)

           2. grid size must be sufficiently big in order to see anything meaningful


Possible improvements/Exploration: 
           1. Scale the window with size of cells in order to get an optimum size window, 
              This will allow the full grid to be seen on every run.

           2. Allow user to click on grid to bring cell alive.

           3. Different cell alive/dead seeding.
"""

import rules as rl
import pygame

# Grid Dimensions (user can change)
rows = 20
cols = 20 

# Define colors
SCREEN_FILL = pygame.color.Color("Black")
CELL_IS_ALIVE = pygame.color.Color("Green")

# Height and width of each cell on grid
HEIGHT = 20
WIDTH = 20
# the distance between cells
MARGIN = 1

# Creates grid 20x20 in this instance 
grid = rl.Grid(rl.make_2D_array(rows, cols))
# print(grid)

# Initialises pygame 
pygame.init()

# Set the HEIGHT and WIDTH of the screen 
WINDOW_SIZE = [460,460]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Creates a title for the screen 
pygame.display.set_caption("Game Of Life")

# Continoues until user closes game  
complete  = False

# Manages how fast the screen updates
screen_update = pygame.time.Clock()

# ---Main Program Loop--- #
while not complete:
	for event in pygame.event.get(): # User perfomed action
		if event.type == pygame.QUIT: # If user clicked close
			complete = True # exit this loop
	
        # Sets color of screen background to black
	screen.fill(SCREEN_FILL)
    
        # Draw the grid 
	for i in range(rows):
		for j in range(cols):
			color = SCREEN_FILL
			if grid[i][j] == 1:
				color = CELL_IS_ALIVE
			pygame.draw.rect(screen,
				color,
				[(MARGIN + WIDTH) * i + MARGIN + 20,
				(MARGIN + HEIGHT) * j * MARGIN + 20,
				WIDTH,
				HEIGHT])
    
        # Limits the frames per second of the screen
	screen_update.tick(30)
    
        # Update screen with what we have drawn
	pygame.display.flip()
    
        # Next grid 
	grid = rl.logic(grid)


pygame.quit()

