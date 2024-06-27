from collections import deque
from heapq import heappush, heappop
from node import Node


class Base:
    def __init__(self):
        self.container = []

    @property
    def empty(self):
        return not self.container

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def __repr__(self):
        return repr(self.container)


class Stack(Base):
    def __init__(self):
        self.container = []


class Queue(Base):
    def __init__(self):
        self.container = deque()

    def pop(self):
        return self.container.popleft()


class PriorityQueue(Base):
    def __init__(self):
        self.container = []

    def push(self, item):
        heappush(self.container, item)

    def pop(self):
        return heappop(self.container)


def dfs(initial, goal_test, successors):
    frontier = Stack()
    frontier.push(Node(initial, None))
    explored = {initial}
    count = 0

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            print(f"dsf_count:{count}")
            return current_node
        for child in successors(current_state):
            count += 1
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


def bfs(initial, goal_test, successors):
    frontier = Queue()
    frontier.push(Node(initial, None))
    explored = {initial}
    count = 0

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            print(f"bfs_count:{count}")
            return current_node
        for child in successors(current_state):
            count += 1
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


def astar(initial, goal_test, successors, heuristic):
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored = {initial: 0.0}
    count = 0

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            print(f"astart_count:{count}")
            return current_node
        for child in successors(current_state):
            count += 1
            new_cost = current_node.cost + 1
            if child in explored and explored[child] <= new_cost:
                continue
            explored[child] = new_cost
            frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None


def node_to_path(node):
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    path.reverse()
    return path


# 柯里化
def euclidean_distance(goal):
    def distance(location):
        xdist = location.column - goal.column
        ydist = location.row - goal.row
        return (xdist**2 + ydist**2) ** 0.5

    return distance


def manhatton_distance(goal):
    def distance(location):
        xdist = abs(location.column - goal.column)
        ydist = abs(location.row - goal.row)
        return xdist + ydist

    return distance


if __name__ == "__main__":
    stack = Stack()
    que = Queue()
    pq = PriorityQueue()
    pq.push(3)
    pq.push(2)
    pq.push(4)
    print(pq)
    pq.pop()
    print(pq)
