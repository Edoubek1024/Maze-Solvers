import pygame
from random import randint
import random
from collections import deque

pygame.init()

GRID_SIZE = 20
SQUARE_SIZE = 25
SPEED = 10  # SPEED can be changed to speed up the visual process

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)


# Line drawing function

def lines(screen, tup, x, y):
    if tup[0]:
        pygame.draw.line(screen, BLACK, (x, y + SQUARE_SIZE), (x + SQUARE_SIZE, y + SQUARE_SIZE), SQUARE_SIZE // 5)
    if tup[1]:
        pygame.draw.line(screen, BLACK, (x, y), (x + SQUARE_SIZE, y), SQUARE_SIZE // 5)
    if tup[2]:
        pygame.draw.line(screen, BLACK, (x, y), (x, y + SQUARE_SIZE), SQUARE_SIZE // 5)
    if tup[3]:
        pygame.draw.line(screen, BLACK, (x + SQUARE_SIZE, y), (x + SQUARE_SIZE, y + SQUARE_SIZE), SQUARE_SIZE // 5)


# New mazes are created by using depth-first search to fill out a grid from a random spot on that grid 
# without overlapping with discovered "cells"

def new_maze(screen):
    start = randint(0, (GRID_SIZE ** 2 - 1))
    discovered = [False] * (GRID_SIZE ** 2)
    todo = [(start, -1)]
    connected = {x: set() for x in range(0, GRID_SIZE ** 2)}
    while todo:
        vertex = todo.pop()
        square = vertex[0]
        if not discovered[square]:
            if vertex[1] != -1:
                connected[vertex[1]].add(square)
                connected[square].add(vertex[1])
            discovered[square] = True
            consider = []
            if square % GRID_SIZE != (GRID_SIZE - 1) and not discovered[square + 1]:
                consider.append(((square + 1), square))
            if square // GRID_SIZE != (GRID_SIZE - 1) and not discovered[square + GRID_SIZE]:
                consider.append(((square + GRID_SIZE), square))
            if square % GRID_SIZE != 0 and not discovered[square - 1]:
                consider.append(((square - 1), square))
            if square // GRID_SIZE != 0 and not discovered[square - GRID_SIZE]:
                consider.append(((square - GRID_SIZE), square))
            random.shuffle(consider)
            todo += consider

    for cell in connected:
        tup = [True, True, True, True]
        if cell + GRID_SIZE in connected[cell]:
            tup[0] = False
        if cell - GRID_SIZE in connected[cell]:
            tup[1] = False
        if cell - 1 in connected[cell]:
            tup[2] = False
        if cell + 1 in connected[cell]:
            tup[3] = False
        x = (cell % GRID_SIZE) * SQUARE_SIZE
        y = (cell // GRID_SIZE) * SQUARE_SIZE
        lines(screen, tup, x, y)
    return connected


# Paths are drawn by using breadth-first search to first determine the fastest path 
# from point A to B (The first blue to purple)

def draw_path(screen, clock, start, graph):
    pygame.draw.line(screen, BLACK, (0, 0), (GRID_SIZE * SQUARE_SIZE - 1, 0), SQUARE_SIZE // 5)
    pygame.draw.line(screen, BLACK, (GRID_SIZE * SQUARE_SIZE - 1, 0),
                     (GRID_SIZE * SQUARE_SIZE - 1, GRID_SIZE * SQUARE_SIZE - 1), SQUARE_SIZE // 5)
    pygame.draw.line(screen, BLACK, (0, (GRID_SIZE * SQUARE_SIZE) - 1),
                     (GRID_SIZE * SQUARE_SIZE - 1, GRID_SIZE * SQUARE_SIZE - 1), SQUARE_SIZE // 5)
    pygame.draw.line(screen, BLACK, (0, 0), (0, GRID_SIZE * SQUARE_SIZE - 1), SQUARE_SIZE // 5)

    # The endpoint of the maze is randomly generated
    end = randint(0, (GRID_SIZE ** 2 - 1))

    # Breadth-first search is used to find the fastest point from A to B
    discovered = deque([start])
    processed = set()
    paths = {start: [start]}
    while discovered:
        if end in discovered:
            break
        node = discovered.popleft()
        if node not in processed:
            processed.add(node)
            for vertex in graph[node]:
                if not vertex == node:
                    paths[vertex] = list(paths[node])
                    paths[vertex].append(vertex)
            discovered += graph[node]

    row = end // GRID_SIZE
    column = end % GRID_SIZE
    x = column * SQUARE_SIZE
    y = row * SQUARE_SIZE
    tup = [True, True, True, True]
    for neighbor in graph[end]:
        if neighbor == end + GRID_SIZE:
            tup[0] = False
        elif neighbor == end - GRID_SIZE:
            tup[1] = False
        elif neighbor == end - 1:
            tup[2] = False
        elif neighbor == end + 1:
            tup[3] = False
    rectangle = ((x, y), (SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, PURPLE, rectangle)
    lines(screen, tup, x, y)
    clock.tick(SPEED)
    pygame.display.flip()

    # The fastest path from point A to point B is now being displayed
    for current_cell in paths[end]:
        row = current_cell // GRID_SIZE
        column = current_cell % GRID_SIZE
        x = column * SQUARE_SIZE
        y = row * SQUARE_SIZE
        tup = [True, True, True, True]
        for neighbor in graph[current_cell]:
            if neighbor == current_cell + GRID_SIZE:
                tup[0] = False
            elif neighbor == current_cell - GRID_SIZE:
                tup[1] = False
            elif neighbor == current_cell - 1:
                tup[2] = False
            elif neighbor == current_cell + 1:
                tup[3] = False
        rectangle = ((x, y), (SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(screen, BLUE, rectangle)
        lines(screen, tup, x, y)
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
        start = randint(0, (GRID_SIZE ** 2 - 1))

        # Mazes are of course randomly generated but, in the right format, 
        # could be predetermined and put into the "new_maze" function as a replacement for "g"
        g = new_maze(screen)
        draw_path(screen, clock, start, g)

        pygame.display.flip()


if __name__ == "__main__":
    main()
