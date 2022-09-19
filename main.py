import pygame
import numpy as np
import sys

def live_cell_counter(A,i,j):
    counter = 0
    pos = [(1,0), (-1,0), (0,1), (0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for p in pos:
        k,l = p
        if A[i+k,l+j]==1:
            counter+=1
    return counter 

age = 0
max_age = 20

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5



# Create a 2 dimensional matrix. A two dimensional
# array is simply a list of lists.
xdim = 10
ydim = 10
grid = np.zeros((xdim,ydim))


# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
#grid[1][5] = 1
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
ws = 255
hs = 300
WINDOW_SIZE = [ws, hs]

screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Game of Life")


pygame.display.update()
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
MOVEEVENT,t = pygame.USEREVENT+1,250
pygame.time.set_timer(MOVEEVENT, t)
flag = 0
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if ws/2-80 <= pos[0] <= ws/2+80 and hs-48 <= pos[1] <= hs-18:
                flag = 1
            else:                
                # Set that location to one
                grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)
        elif event.type == MOVEEVENT and flag == 1:
            for i in range(2,xdim-1):
                for j in range(2,ydim-1):
                    live_cells = live_cell_counter(grid,i,j)
                    if live_cells < 2:
                        grid[i,j] = 0
                    elif live_cells < 3 and live_cells < 2 and grid[i,j]==1:
                        grid[i,j] = 1
                    elif live_cells > 3:
                        grid[i,j]=0
                    elif live_cells == 3 and grid[i,j]==0:
                        grid[i,j]=1

 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    # Set button
    wh = (255,255,255)
    smallfont = pygame.font.SysFont('Corbel',36)
    text = smallfont.render('Start' , True , wh)
    screen.blit(text , (ws/2-25,hs-38))
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()



# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()