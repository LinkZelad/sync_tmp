import random
from collections import deque, namedtuple
from enum import Enum

from node import Node
from searchs import (
    Stack,
    Queue,
    PriorityQueue,
    bfs,
    dfs,
    astar,
    node_to_path,
    manhatton_distance,
)


class Cell(str, Enum):
    EMPTY = " "
    WALL = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


MazeLocation = namedtuple("MazeLocation", ["row", "column"])


class Maze:
    def __init__(
        self,
        row=10,
        column=10,
        start=MazeLocation(0, 0),
        goal=MazeLocation(9, 9),
        spraseness=0.2,
    ):
        self.row = row
        self.column = column
        self.start = start
        self.goal = goal
        self.spraseness = spraseness

        self.grid = [[Cell.EMPTY for c in range(column)] for r in range(row)]
        self._randomy_fill()
        self.grid[start.row][start.column] = Cell.START
        self.grid[goal.row][goal.column] = Cell.GOAL

    def _randomy_fill(self):
        for r in range(self.row):
            for c in range(self.column):
                if random.uniform(0, 1) < self.spraseness:
                    self.grid[r][c] = Cell.WALL

    def __str__(self):
        output = ""
        for row in self.grid:
            output += "".join([cell.value for cell in row]) + "\n"
        return output

    def successor(self, current: MazeLocation):
        location = []
        if (
            current.row + 1 < self.row
            and self.grid[current.row + 1][current.column] != Cell.WALL
        ):
            location.append(MazeLocation(current.row + 1, current.column))
        if (
            current.row - 1 >= 0
            and self.grid[current.row - 1][current.column] != Cell.WALL
        ):
            location.append(MazeLocation(current.row - 1, current.column))
        if (
            current.column + 1 < self.column
            and self.grid[current.row][current.column + 1] != Cell.WALL
        ):
            location.append(MazeLocation(current.row, current.column + 1))
        if (
            current.column - 1 >= 0
            and self.grid[current.row][current.column - 1] != Cell.WALL
        ):
            location.append(MazeLocation(current.row, current.column - 1))
        return location

    def goal_test(self, location):
        return self.goal == location

    def mark(self, path):
        for location in path:
            self.grid[location.row][location.column] = Cell.PATH
        self.grid[self.start.row][self.start.column] = Cell.START
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path):
        for location in path:
            self.grid[location.row][location.column] = Cell.EMPTY
        self.grid[self.start.row][self.start.column] = Cell.START
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL


if __name__ == "__main__":
    maze = Maze()
    print(maze)
    print("-" * 10)
    solutions1 = dfs(maze.start, maze.goal_test, maze.successor)
    path = []
    if solutions1:
        path = node_to_path(solutions1)
        maze.mark(path)
        print(maze)
    else:
        print("No solution")

    maze.clear(path)
    solutions2 = bfs(maze.start, maze.goal_test, maze.successor)
    if solutions2:
        path = node_to_path(solutions2)
        maze.mark(path)
        print(maze)
    else:
        print("No solution")

    maze.clear(path)
    solutions3 = astar(
        maze.start, maze.goal_test, maze.successor, manhatton_distance(maze.goal)
    )
    if solutions2:
        path = node_to_path(solutions3)
        maze.mark(path)
        print(maze)
    else:
        print("No solution")
