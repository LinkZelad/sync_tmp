from __future__ import annotations
from graph import Graph
from weight_edge import WeightEdge
from typing import TypeVar, List, Tuple, Callable

V = TypeVar('V')

class WeightGraph(Graph):
    def __init__(self, vertices:List[V]=None):
        if vertices is None:
            vertices = []

        self.vertices: List[V] = vertices
        self.edges: List[List[WeightEdge]] = [[] for _ in vertices]


    def add_edge_by_indices(self, f_index: int, t_index: int, weight: float) -> bool:
        if f_index >= self.vertex_count or t_index >= self.vertex_count:
            print(f"The index must be in {self.vertex_count}!")
            return False
        edge = WeightEdge(f_index, t_index, weight)
        self.edges[f_index].append(edge)
        self.edges[t_index].append(edge.reversed())
        return True

    def add_edge_by_vertices(self, f_v: V, t_v: V, weight: float) -> None:
        if f_v not in self.vertices:
            self.add_vertex(f_v)
        if t_v not in self.vertices:
            self.add_vertex(t_v)
        f_int = self.index_of_vertex(f_v)
        t_int = self.index_of_vertex(t_v)
        edge: WeightEdge = WeightEdge(f_int, t_int, weight)
        self.add_edge(edge)


    def neighbors_of_index_with_weight(self, f_index: int) -> List[Tuple[int, float]]:
        return [(self.vertex_at(e.t), e.weight) for e in self.edges[f_index]]

    def neighbors_of_vertex_with_weight(self, v: V) -> List[Tuple[int, float]]:
        return self.neighbors_of_index_with_weight(self.index_of_vertex(v))

    def __str__(self):
        desc: str = ""
        desc += f"Vertices: {self.vertices}\n"
        desc += f"Vertex count: {self.vertex_count}\n"
        desc += "Edges:\n\033[31m"
        for i in range(self.vertex_count):
            desc += f"    {self.vertices[i]} --> {self.neighbors_of_index_with_weight(i)}\n"
        desc += "\033[0m"
        return desc

if __name__ == '__main__':
    city_graph2: WeightGraph[str] = WeightGraph(
        ["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston", "New York", "Atlanta",
         "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])
    city_graph2.add_edge_by_vertices("Seattle", "Chicago", 1737)
    city_graph2.add_edge_by_vertices("Seattle", "San Francisco", 678)
    city_graph2.add_edge_by_vertices("San Francisco", "Riverside", 386)
    city_graph2.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
    city_graph2.add_edge_by_vertices("Los Angeles", "Riverside", 50)
    city_graph2.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
    city_graph2.add_edge_by_vertices("Riverside", "Phoenix", 307)
    city_graph2.add_edge_by_vertices("Riverside", "Chicago", 1704)
    city_graph2.add_edge_by_vertices("Phoenix", "Dallas", 887)
    city_graph2.add_edge_by_vertices("Phoenix", "Houston", 1015)
    city_graph2.add_edge_by_vertices("Dallas", "Chicago", 805)
    city_graph2.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph2.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph2.add_edge_by_vertices("Houston", "Atlanta", 702)
    city_graph2.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph2.add_edge_by_vertices("Atlanta", "Chicago", 588)
    city_graph2.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph2.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph2.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph2.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph2.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph2.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph2.add_edge_by_vertices("Detroit", "New York", 482)
    city_graph2.add_edge_by_vertices("Boston", "New York", 190)
    city_graph2.add_edge_by_vertices("New York", "Philadelphia", 81)
    city_graph2.add_edge_by_vertices("Philadelphia", "Washington", 123)

    import sys
    sys.path.append("../../ch2")
    from node import Node
    from searchs import node_to_path,PriorityQueue

    def heuristic(v:V):
        return 0

    def astar(initial, goal_test, successors, heuristic):
        frontier = PriorityQueue()
        frontier.push(Node(initial, None, 0.0, heuristic(initial)))
        explored = {initial: 0.0}

        while not frontier.empty:
            current_node = frontier.pop()
            current_state = current_node.state
            print(f"{current_state} pop current cost {current_node.cost}\033[33m")
            if goal_test(current_state):
                return current_node
            for child, weight in successors(current_state):
                new_cost = current_node.cost + weight
                if child in explored and explored[child] <= new_cost:
                    print(f"{child} pass")
                    continue
                print(f"{child} push cost {new_cost}")
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
            print("\033[0m")
        return None

    solution = astar("Los Angeles", lambda x: x == "Atlanta", city_graph2.neighbors_of_vertex_with_weight, heuristic)
