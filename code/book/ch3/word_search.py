# bug 不能有相同元素
from typing import NamedTuple

from csp import CSP,Constraint
from string import ascii_uppercase
from random import choice

Grid = []

GridLocation = NamedTuple("GridLocation", [("row", int), ("column", int)])

def generate_grid(rows, columns):
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]

def display_grid(grid):
    for row in grid:
        print("".join(row))

def generate_domain(word, grid):
    domain = []
    height = len(grid)
    width = len(grid[0])
    length = len(word)
    for r in range(height):
        for c in range(width):
            columns = range(c, c + length + 1)
            rows = range(r, r + length + 1)
            if c + length <= width:
                domain.append([GridLocation(r, co) for co in columns])
                if r + length <= length:
                    domain.append([GridLocation(r + (c - co), co) for co in columns])
            if r + length <= length:
                domain.append([GridLocation(ro, c) for ro in rows])
                if c - length >= 0:
                    domain.append([GridLocation(ro, c - (r - ro)) for ro in rows])
    return domain

class Wordsearchconstraint(Constraint):
    def __init__(self, words):
        super().__init__(words)
        self.words = words

    def satisfied(self, assignment):
        all_locations = [locs for values in assignment.values() for locs in values]
        return len(set(all_locations)) == len(all_locations)


if __name__ == '__main__':
    grid = generate_grid(9, 9)
    words = ["MATTHEW", "JOE", "MARY", "SARAH", "SANTO"]
    locations = {}
    for word in words:
        locations[word] = generate_domain(word, grid)

    csp = CSP(words, locations)
    csp.add_constraint(Wordsearchconstraint(words))
    solution = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        for word, grid_locations in solution.items():
            if choice([True, False]):
                grid_locations.reverse()
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter.lower()

        display_grid(grid)