import pygame
from random import randint
import random
from collections import deque

pygame.init()

GRID_SIZE = 20
SQUARE_SIZE = 25
SPEED = 10 #SPEED can be changed to speed up the visual process

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)

# Line drawing function

def lines(screen, clock, tup, x, y):
  if tup[0]:
    pygame.draw.line(screen, BLACK, (x, y + SQUARE_SIZE), (x + SQUARE_SIZE, y + SQUARE_SIZE), SQUARE_SIZE // 5)
  if tup[1]:
    pygame.draw.line(screen, BLACK, (x, y), (x + SQUARE_SIZE, y), SQUARE_SIZE // 5)
  if tup[2]:
    pygame.draw.line(screen, BLACK, (x, y), (x, y + SQUARE_SIZE), SQUARE_SIZE // 5)
  if tup[3]:
    pygame.draw.line(screen, BLACK, (x + SQUARE_SIZE, y), (x + SQUARE_SIZE, y + SQUARE_SIZE), SQUARE_SIZE // 5)
 
# New mazes are created by using depth-first search to fill out a grid from a random spot on that grid without overlapping with discovered "cells"

def new_maze(screen, clock):
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
 
  for m in connected:
    tup = [True, True, True, True]
    if m + GRID_SIZE in connected[m]:
      tup[0] = False
    if m - GRID_SIZE in connected[m]:
      tup[1] = False
    if m - 1 in connected[m]:
      tup[2] = False
    if m + 1 in connected[m]:
      tup[3] = False
    x = (m % GRID_SIZE) * SQUARE_SIZE
    y = (m // GRID_SIZE) * SQUARE_SIZE
    lines(screen, clock, tup, x, y)
  return connected

# Paths are drawn by using breadth-first search to first determine the fastest path from point A to B (The first blue to purple)

def draw_path(screen, clock, start, graph):
    pygame.draw.line(screen, BLACK, (0, 0), (GRID_SIZE * SQUARE_SIZE - 1, 0), SQUARE_SIZE // 5)
    pygame.draw.line(screen, BLACK, (GRID_SIZE * SQUARE_SIZE - 1, 0), (GRID_SIZE * SQUARE_SIZE - 1, GRID_SIZE * SQUARE_SIZE - 1), SQUARE_SIZE // 5)
    pygame.draw.line(screen, BLACK, (0, (GRID_SIZE * SQUARE_SIZE) - 1), (GRID_SIZE * SQUARE_SIZE - 1, GRID_SIZE * SQUARE_SIZE - 1), SQUARE_SIZE // 5)
    pygame.draw.line(screen, BLACK, (0, 0), (0, GRID_SIZE * SQUARE_SIZE - 1), SQUARE_SIZE // 5)

    # The endpoint of the maze is randomly generated
    end = randint(0, (GRID_SIZE**2 - 1))

    # Breadth-first search is used to find the fastest point from A to B
    discovered = deque([start])
    processed = set()
    paths = {start: [start]}
    while discovered:
      if end in discovered:
        break
      n = discovered.popleft()
      if not n in processed:
        processed.add(n)
        for v in graph[n]:
          if not v == n:
            paths[v] = list(paths[n])
            paths[v].append(v)
        discovered += graph[n]
   
    row = end // GRID_SIZE
    column = end % GRID_SIZE
    x = column * SQUARE_SIZE
    y = row * SQUARE_SIZE
    tup = [True, True, True, True]
    for j in graph[end]:
      if j == end + GRID_SIZE:
        tup[0] = False
      elif j == end - GRID_SIZE:
        tup[1] = False
      elif j == end - 1:
        tup[2] = False
      elif j == end + 1:
        tup[3] = False
    RECTANGLE = ((x, y), (SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, PURPLE, RECTANGLE)
    lines(screen, clock, tup, x, y)
    clock.tick(SPEED)
    pygame.display.flip()

    #The fastest path from point A to point B is now being displayed
    for i in paths[end]:
      row = i // GRID_SIZE
      column = i % GRID_SIZE
      x = column * SQUARE_SIZE
      y = row * SQUARE_SIZE
      tup = [True, True, True, True]
      for j in graph[i]:
          if j == i + GRID_SIZE:
            tup[0] = False
          elif j == i - GRID_SIZE:
            tup[1] = False
          elif j == i - 1:
            tup[2] = False
          elif j == i + 1:
            tup[3] = False
      RECTANGLE = ((x, y), (SQUARE_SIZE, SQUARE_SIZE))
      pygame.draw.rect(screen, BLUE, RECTANGLE)
      lines(screen, clock, tup, x, y)
      clock.tick(SPEED)
      pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE))

    # This continuously makes new mazes to be solved
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
               
               
        screen.fill(WHITE)
        start = randint(0, (GRID_SIZE**2 - 1))

        # Mazes are of course randomly generated but, in the right format, could be predetermined and put into the "new_maze" function as a replacement for "g"
        g = new_maze(screen, clock)
        draw_path(screen, clock, start, g)

        pygame.display.flip()

if __name__ == "__main__":
    main()
