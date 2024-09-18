# Maze Solvers

Maze Solvers contains a group of python files which all utilize the pygame library to display a use of a maze. These files each show different methods of both breadth-first search and depth-first search to achieve certain goals.

## The Maze
All files in this repository use the function `new_maze` to generate a new random maze. Using a square grid of cells based on a given size, a maze is generated by using depth-first search, starting at a random cell, to randomly move throughout the grid. Since this is done through depth-first search, connections to other cells are only formed if the target cell is undiscovered. Should the movement find a cell that has already been discovered or processed, it will not make a connection to it. Some of the solvers will display this lack of a connection as a wall between cells. This method allows for a complete maze without any cells that cannot be found to be created and used.

## Breadth-First Search Filler
This solver, under the file name `Breadth-First-Search-Random-Maze-Filler.py`, uses the breadth-first search method to fill in a maze. Starting from a randomly selected cell, the algorithm moves throughout the maze in equally long paths until the maze is filled. This is done by putting processing priority on cells that have been discovered the earliest. To visualize this, discovered but unprocessed cells are painted blue, cells being processed are painted red, and processed cells are painted green. Once every cell has been processed in the maze, which will be displayed by an entirely green maze, a new maze is generated and the cycle repeats. This simple use of the breadth-first search method can be used as a good example of the algorithm and how it can be used.

![image](https://github.com/user-attachments/assets/07198f49-4908-4dea-a824-c6fff76f05bc)

## Depth-First Search Filler
This solver, under the file name `Depth-First-Search-Random-Maze-Filler.py`, uses the depth-first search method to fill in a maze. Unlike the breadth-first search filler, this filler only displays the walls of the maze once they are discovered. Starting from a randomly selected cell, the algorithm moves throughout the maze until it hits a dead end. Once a dead end is hit, the algorithm processes previous cells, putting priority on the most recent cells discovered. This priority of deeper cells over shallower cells is the difference betweeen depth-first search and breadth-first search. To visualize the process, unprocessed cells are painted blue, cells being processed are painted red, and processed cells are painted green. Once every cell has been processed in the maze, which will be displayed by an entirely green maze, a new maze is generated and the cycle repeats.

![image](https://github.com/user-attachments/assets/c3140d27-5afd-4e32-bb9d-d3de584b1097)

## A-to-B Path Solver
This solver, under the name `Maze-Solver-A-to-B.py`, uses the breadth-first search method to display the fastest route in a maze from one randomly selected cell to another randomly selected cell. Since breadth-first search uses equal length paths to explore the maze, the path that finds the target first is the fastest. The determination of this route is done without display but the route is displayed in the maze. Displayed in a growing snake-like way, the route starting at one cell is painted blue while the target cell is painted purple. Upon the route's arrival to the target cell, which is visualized by the target cell turning blue, a new maze and random cells are generated and the cycle repeats.

![image](https://github.com/user-attachments/assets/577e686e-2459-4b6f-9757-4df89aaaa359)
