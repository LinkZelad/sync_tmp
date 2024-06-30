from csp import CSP, Constraint
from typing import NamedTuple, List, Dict
from math import ceil

Soku_Location = NamedTuple("Soku_Location", [("row", int), ("column", int)])

def generate_sokudo():
    soku_grid  = [Soku_Location(row, column) for row in range(9) for column in range(9)]
    return soku_grid
def check_soku(location1, location2):
    if location1.row == location2.row or location1.column == location2.column:
        return True
    if ceil((location1.row + 1) / 3) == ceil((location2.row + 1) / 3) and ceil((location1.column + 1) / 3) == ceil((location2.column + 1) / 3):
        return True
    return False
class SokuConstraint(Constraint[Soku_Location, int]):
    def __init__(self, locations: List[Soku_Location]) -> None:
        super().__init__(locations)
        self.locations = locations

    def satisfied(self, assignment: Dict[Soku_Location, int]) -> bool:
        for location1 in assignment:
            assignment_copy = assignment.copy()
            del assignment_copy[location1]
            for location2 in assignment_copy:
                if check_soku(location1, location2):
                    if assignment[location1] == assignment[location2]:
                        return False
        return True

def make_min_clues():
    clues = {
        Soku_Location(0, 3): 8,
        Soku_Location(0, 5): 1,
        Soku_Location(1, 7): 4,
        Soku_Location(1, 8): 3,
        Soku_Location(2, 0): 5,
        Soku_Location(3, 4): 7,
        Soku_Location(3, 6): 8,
        Soku_Location(4, 6): 1,
        Soku_Location(5, 1): 2,
        Soku_Location(5, 4): 3,
        Soku_Location(6, 0): 6,
        Soku_Location(6, 7): 7,
        Soku_Location(6, 8): 5,
        Soku_Location(7, 2): 3,
        Soku_Location(7, 3): 4,
        Soku_Location(8, 3): 2,
        Soku_Location(8, 6): 6,
    }
    return clues
def make_clues_easy():
    clues = {
        Soku_Location(0, 2): 3,
        Soku_Location(0, 5): 7,
        Soku_Location(0, 8): 5,
        Soku_Location(1, 0): 4,
        Soku_Location(1, 1): 5,
        Soku_Location(1, 3): 9,
        Soku_Location(1, 4): 1,
        Soku_Location(2, 3): 5,
        Soku_Location(2, 6): 6,
        Soku_Location(2, 7): 4,
        Soku_Location(2, 8): 8,
        Soku_Location(3, 0): 5,
        Soku_Location(3, 3): 7,
        Soku_Location(3, 5): 1,
        Soku_Location(3, 7): 3,
        Soku_Location(3, 8): 4,
        Soku_Location(4, 2): 1,
        Soku_Location(4, 3): 2,
        Soku_Location(4, 5): 4,
        Soku_Location(4, 6): 7,
        Soku_Location(5, 0): 6,
        Soku_Location(5, 1): 4,
        Soku_Location(5, 3): 3,
        Soku_Location(5, 5): 8,
        Soku_Location(5, 8): 9,
        Soku_Location(6, 0): 8,
        Soku_Location(6, 1): 2,
        Soku_Location(6, 2): 5,
        Soku_Location(6, 5): 9,
        Soku_Location(7, 4): 2,
        Soku_Location(7, 5): 5,
        Soku_Location(7, 7): 8,
        Soku_Location(7, 8): 7,
        Soku_Location(8, 0): 9,
        Soku_Location(8, 3): 6,
        Soku_Location(8, 6): 5,
    }
    return clues

if __name__ == '__main__':
    soku_grid = generate_sokudo()
    domain = {}
    for location in soku_grid:
        domain[location] = [i for i in range(1, 10)]
    clues = make_min_clues()
    # clues = make_clues_easy()
    # for location, value in clues.items():
    #     domain[location] = [value]

    csp = CSP(soku_grid, domain)

    csp.add_constraint(SokuConstraint(soku_grid))
    import time
    t0 = time.time()
    solution = csp.backtracking_search(assignment=clues)
    if solution is None:
        print("No solution found!")
    else:
        for i in range(9):
            for j in range(9):
                print(solution[Soku_Location(i, j)], end=" ")
            print("\n")

    print(time.time() - t0)