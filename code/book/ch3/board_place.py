# bug 不能有相同元素，需要修复
from csp import CSP, Constraint
from typing import NamedTuple

Grid = []

GridLocation = NamedTuple("GridLocation", [("row", int), ("column", int)])

def generate_grid(rows, columns):
    return [["*" for c in range(columns)] for r in range(rows)]

def display_grid(grid):
    for row in grid:
        print("".join(row))

def generate_domain(scale, grid):
    domain = []
    height = len(grid)
    width = len(grid[0])
    w, h = scale

    for r in range(height):
        for c in range(width):
            columns = range(c, c + w)
            rows = range(r, r + h )
            if c + w <= width:
                if r + h <= height:
                    domain.append([GridLocation(ro, co) for co in columns for ro in rows])
                if r - h >= 0:
                    domain.append([GridLocation(r - i, co) for co in columns for i in range(h)])

            if c - w >= 0:
                if r + h <= height:
                    domain.append([GridLocation(ro, c - i) for ro in rows for i in range(w)])
                if r - h >= 0:
                    domain.append([GridLocation(r - i, c - j) for i in range(h) for j in range(w)])
    return domain

class BoardPlaceConstraint(Constraint):
    def __init__(self, scalse):
        super().__init__(scalse)
        self.words = scalse

    def satisfied(self, assignment):
        all_locations = [locs for values in assignment.values() for locs in values]
        return len(set(all_locations)) == len(all_locations)


if __name__ == '__main__':
    grid = generate_grid(10, 10)
    words = [(1,3), (5,2), (2,6), (8,3), (4,7)]
    locations = {}
    for word in words:
        locations[word] = generate_domain(word, grid)

    csp = CSP(words, locations)
    csp.add_constraint(BoardPlaceConstraint(words))
    solution = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        for key, value in solution.items():
            for location in value:
                (row, col) = (location.row, location.column)
                grid[row][col] = f"{key[0]}"
        display_grid(grid)
