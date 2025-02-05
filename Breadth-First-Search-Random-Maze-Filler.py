import pygame
from random import randint
import random
from collections import deque

pygame.init()

GRID_SIZE = 20
SQUARE_SIZE = 25
SPEED = 9999

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


def lines(screen, tup, x, y):
    if tup[0]:
        pygame.draw.line(screen, BLACK, (x, y + SQUARE_SIZE), (x + SQUARE_SIZE, y + SQUARE_SIZE), SQUARE_SIZE // 5)
    if tup[1]:
        pygame.draw.line(screen, BLACK, (x, y), (x + SQUARE_SIZE, y), SQUARE_SIZE // 5)
    if tup[2]:
        pygame.draw.line(screen, BLACK, (x, y), (x, y + SQUARE_SIZE), SQUARE_SIZE // 5)
    if tup[3]:
        pygame.draw.line(screen, BLACK, (x + SQUARE_SIZE, y), (x + SQUARE_SIZE, y + SQUARE_SIZE), SQUARE_SIZE // 5)


def new_maze(screen):
    # New mazes are created by using depth-first search
    # to fill out a grid from a random spot on that grid without overlapping with discovered "cells"

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

    for neighbor in connected:
        tup = [True, True, True, True]
        if neighbor + GRID_SIZE in connected[neighbor]:
            tup[0] = False
        if neighbor - GRID_SIZE in connected[neighbor]:
            tup[1] = False
        if neighbor - 1 in connected[neighbor]:
            tup[2] = False
        if neighbor + 1 in connected[neighbor]:
            tup[3] = False
        x = (neighbor % GRID_SIZE) * SQUARE_SIZE
        y = (neighbor // GRID_SIZE) * SQUARE_SIZE
        lines(screen, tup, x, y)
    return connected


def draw_maze(screen, clock, start, graph):
    # Green squares mark fully processed "cells",
    # blue squares mark discovered but not processed "cells",
    # and the black lines represent the walls blocking movement from each "cell"
    # Breadth-first search is used to fill this maze in a more "hesitant" manner than the depth-first search method

    pygame.draw.line(screen, BLACK, (0, 0), (GRID_SIZE * SQUARE_SIZE - 1, 0), SQUARE_SIZE // 5)
    pygame.draw.line(screen, BLACK, (GRID_SIZE * SQUARE_SIZE - 1, 0),
                     (GRID_SIZE * SQUARE_SIZE - 1, GRID_SIZE * SQUARE_SIZE - 1), SQUARE_SIZE // 5)
    pygame.draw.line(screen, BLACK, (0, (GRID_SIZE * SQUARE_SIZE) - 1),
                     (GRID_SIZE * SQUARE_SIZE - 1, GRID_SIZE * SQUARE_SIZE - 1), SQUARE_SIZE // 5)
    pygame.draw.line(screen, BLACK, (0, 0), (0, GRID_SIZE * SQUARE_SIZE - 1), SQUARE_SIZE // 5)
    discovered = [False] * (len(graph))
    processed = [False] * (len(graph))
    todo = deque([start])
    connected = {}
    while todo:
        square = todo.popleft()
        row = square // GRID_SIZE
        column = square % GRID_SIZE
        x = column * SQUARE_SIZE
        y = row * SQUARE_SIZE
        rectangle = ((x, y), (SQUARE_SIZE, SQUARE_SIZE))
        pygame.display.flip()
        tup = [True, True, True, True]
        pygame.draw.rect(screen, RED, rectangle)
        clock.tick(SPEED)
        pygame.display.flip()
        if discovered[square] and not processed[square]:
            tup = list(connected[square])
            pygame.draw.rect(screen, GREEN, rectangle)
            lines(screen, tup, x, y)
            clock.tick(SPEED)
            pygame.display.flip()
            processed[square] = True
        elif not discovered[square]:
            discovered[square] = True
            todo.append(square)
            for neighbor in graph[square]:
                if neighbor == square + GRID_SIZE:
                    tup[0] = False
                elif neighbor == square - GRID_SIZE:
                    tup[1] = False
                elif neighbor == square - 1:
                    tup[2] = False
                elif neighbor == square + 1:
                    tup[3] = False
                if not discovered[neighbor]:
                    todo.append(neighbor)
            connected[square] = list(tup)
            pygame.draw.rect(screen, BLUE, rectangle)
            lines(screen, tup, x, y)
            clock.tick(SPEED)
            pygame.display.flip()


def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(WHITE)
        start = randint(0, (GRID_SIZE ** 2 - 1))
        g = new_maze(screen)
        draw_maze(screen, clock, start, g)

        pygame.display.flip()


if __name__ == "__main__":
    main()
