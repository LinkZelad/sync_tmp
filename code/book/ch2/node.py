class Node:
    def __init__(self, state, parent, cost=0.0, heuristic=0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


if __name__ == "__main__":
    pass
