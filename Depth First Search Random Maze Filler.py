import pygame
from random import randint
import random

pygame.init()

GRID_SIZE = 100
SQUARE_SIZE = 5
SPEED = float('inf')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

def lines(screen, clock, tup, x, y):
  if tup[0]:
    pygame.draw.line(screen, BLACK, (x, y + SQUARE_SIZE), (x + SQUARE_SIZE, y + SQUARE_SIZE), SQUARE_SIZE // 5)
  if tup[1]:
    pygame.draw.line(screen, BLACK, (x, y), (x + SQUARE_SIZE, y), SQUARE_SIZE // 5)
  if tup[2]:
    pygame.draw.line(screen, BLACK, (x, y), (x, y + SQUARE_SIZE), SQUARE_SIZE // 5)
  if tup[3]:
    pygame.draw.line(screen, BLACK, (x + SQUARE_SIZE, y), (x + SQUARE_SIZE, y + SQUARE_SIZE), SQUARE_SIZE // 5)
  clock.tick(SPEED)
  pygame.display.flip()

def new_maze():

# New mazes are created by using depth-first search to fill out a grid from a random spot on that grid without overlapping with discovered "cells"

  start = randint(0, (GRID_SIZE**2 - 1))
  discovered = [False]*(GRID_SIZE**2)
  processed = [False]*(GRID_SIZE**2)
  todo = [(start, -1)]
  connected = {x: set() for x in range(0, GRID_SIZE**2)}
  while todo:
      v = todo.pop()
      s = v[0]
      if not discovered[s]:
        if v[1] != -1:
          connected[v[1]].add(s)
          connected[s].add(v[1])
        discovered[s] = True
        cons = []
        if s % GRID_SIZE != (GRID_SIZE - 1) and not discovered[s + 1]:
          cons.append(((s + 1), s))
        if s // GRID_SIZE != (GRID_SIZE - 1) and not discovered[s + GRID_SIZE]:
          cons.append(((s + GRID_SIZE), s))
        if s % GRID_SIZE != 0 and not discovered[s - 1]:
          cons.append(((s - 1), s))
        if s // GRID_SIZE != 0 and not discovered[s - GRID_SIZE]:
          cons.append(((s - GRID_SIZE), s))
        random.shuffle(cons)
        todo += cons
       
  return connected

def draw_maze(screen, clock, start, graph):

# To visually show the maze being drawn, I used pygame to display the solver discovering walls as it moves throughout the invisible maze.
# The intention was to make it look as if a person who was plopped into a random maze were filling out their own map of said maze.
# Green squares mark fully processed "cells", blue squares mark discovered but not processed "cells", and the black lines represent the walls blocking movement from each "cell"

    pygame.draw.line(screen, BLACK, (0, 0), (GRID_SIZE * SQUARE_SIZE - 1, 0), SQUARE_SIZE // 5)
    pygame.draw.line(screen, BLACK, (GRID_SIZE * SQUARE_SIZE - 1, 0), (GRID_SIZE * SQUARE_SIZE - 1, GRID_SIZE * SQUARE_SIZE - 1), SQUARE_SIZE // 5)
    pygame.draw.line(screen, BLACK, (0, (GRID_SIZE * SQUARE_SIZE) - 1), (GRID_SIZE * SQUARE_SIZE - 1, GRID_SIZE * SQUARE_SIZE - 1), SQUARE_SIZE // 5)
    pygame.draw.line(screen, BLACK, (0, 0), (0, GRID_SIZE * SQUARE_SIZE - 1), SQUARE_SIZE // 5)

# This depth-first search algorithm both does all of the jobs said above and also displays the "cells" in their updated states
    discovered = [False]*(len(graph))
    processed = [False]*(len(graph))
    todo = [(start)]
    connected = {}
    while todo:
      s = todo.pop()
      row = s // GRID_SIZE
      column = s % GRID_SIZE
      x = column * SQUARE_SIZE
      y = row * SQUARE_SIZE
      RECTANGLE = ((x, y), (SQUARE_SIZE, SQUARE_SIZE))
      pygame.display.flip()
      tup = [True, True, True, True]
      pygame.draw.rect(screen, RED, RECTANGLE)
      clock.tick(SPEED)
      pygame.display.flip()
      if discovered[s] and not processed[s]:
        tup = list(connected[s])
        pygame.draw.rect(screen, GREEN, RECTANGLE)
        lines(screen, clock, tup, x, y)
        processed[s] = True
      elif not discovered[s]:
        discovered[s] = True
        todo.append(s)
        for i in graph[s]:
          if i == s + GRID_SIZE:
            tup[0] = False
          elif i == s - GRID_SIZE:
            tup[1] = False
          elif i == s - 1:
            tup[2] = False
          elif i == s + 1:
            tup[3] = False
          if not discovered[i]:
            todo.append(i)
        connected[s] = list(tup)
        pygame.draw.rect(screen, BLUE, RECTANGLE)
        lines(screen, clock, tup, x, y)

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
               
               
        screen.fill(WHITE)
        start = randint(0, (GRID_SIZE**2 - 1)) # Picks random starting point for the filler
        g = new_maze() # Generates a new maze to fill
        draw_maze(screen, clock, start, g) # Fills maze


if __name__ == "__main__":
    main()
