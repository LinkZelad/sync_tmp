from __future__ import annotations

from typing import (List, Dict, TypeVar, Callable)

from edge import Edge

# verext maybe str,int..
V = TypeVar('V')

"""
f means from, t means to
"""


class Graph:
    def __init__(self, vertices=None):
        if vertices is None:
            vertices = []
        self.vertices: List[V] = vertices
        self.edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self.vertices)

    @property
    def edge_count(self) -> int:
        return sum(map(len, self.edges))

    def add_vertex(self, v: V) -> int:
        if v in self.vertices:
            print(f"{v} has exists in Graph!")
            return -1
        self.vertices.append(v)
        self.edges.append([])
        return self.vertex_count - 1

    def add_edge(self, e: Edge) -> None:
        self.edges[e.f].append(e)
        self.edges[e.t].append(e.reversed())

    def add_edge_by_vertices(self, f_v: V, t_v: V) -> None:
        if f_v not in self.vertices:
            self.add_vertex(f_v)
        if t_v not in self.vertices:
            self.add_vertex(t_v)
        f_int = self.index_of_vertex(f_v)
        t_int = self.index_of_vertex(t_v)
        edge = Edge(f_int, t_int)
        self.add_edge(edge)

    def add_edge_by_indices(self, f_index: int, t_index: int) -> bool:
        if f_index >= self.vertex_count or t_index >= self.vertex_count:
            print(f"The index must be in {self.vertex_count}!")
            return False
        edge = Edge(f_index, t_index)
        self.add_edge(edge)
        return True

    def vertex_at(self, index) -> int:
        return self.vertices[index]

    def index_of_vertex(self, v: V) -> V:
        return self.vertices.index(v)

    def neighbors_of_index(self, f_index: int) -> List[V]:
        return [self.vertex_at(e.t) for e in self.edges[f_index]]

    def neighbors_of_vertex(self, v: V) -> List[V]:
        return self.neighbors_of_index(self.index_of_vertex(v))

    def edges_of_index(self, index: int):
        return self.edges[index]

    def edges_of_vertex(self, vertex: V):
        return self.edges_of_index(self.index_of_vertex(vertex))

    def __str__(self):
        desc: str = ""
        desc += f"Vertices: {self.vertices}\n"
        desc += f"Vertex count: {self.vertex_count}\n"
        desc += "Edges:\n\033[31m"
        for i in range(self.vertex_count):
            # desc += f"    {self.vertex_at(i)} --> {[self.vertex_at(e.t) for e in self.edges[i]]}\n"
            desc += f"    {self.vertex_at(i)} --> {self.neighbors_of_index(i)}\n"
        # for v in self.vertices:
        #     desc += f"    {v} --> {[self.vertex_at(e.t) for e in self.edges[self.index_of_vertex(v)]]}\n"
        desc += "\033[0m"
        return desc


if __name__ == '__main__':
    city_graph: Graph[str] = Graph(
        ["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston", "New York", "Atlanta",
         "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Chicago")
    city_graph.add_edge_by_vertices("Phoenix", "Dallas")
    city_graph.add_edge_by_vertices("Phoenix", "Houston")
    city_graph.add_edge_by_vertices("Dallas", "Chicago")
    city_graph.add_edge_by_vertices("Dallas", "Atlanta")
    city_graph.add_edge_by_vertices("Dallas", "Houston")
    city_graph.add_edge_by_vertices("Houston", "Atlanta")
    city_graph.add_edge_by_vertices("Houston", "Miami")
    city_graph.add_edge_by_vertices("Atlanta", "Chicago")
    city_graph.add_edge_by_vertices("Atlanta", "Washington")
    city_graph.add_edge_by_vertices("Atlanta", "Miami")
    city_graph.add_edge_by_vertices("Miami", "Washington")
    city_graph.add_edge_by_vertices("Chicago", "Detroit")
    city_graph.add_edge_by_vertices("Detroit", "Boston")
    city_graph.add_edge_by_vertices("Detroit", "Washington")
    city_graph.add_edge_by_vertices("Detroit", "New York")
    city_graph.add_edge_by_vertices("Boston", "New York")
    city_graph.add_edge_by_vertices("New York", "Philadelphia")
    city_graph.add_edge_by_vertices("Philadelphia", "Washington")

    from collections import deque

    from dataclasses import dataclass

    T = TypeVar("T")


    @dataclass
    class Node:
        current_content: T
        parent_node: Node | None


    class Queue:
        def __init__(self):
            self.container = deque()

        @property
        def is_empty(self) -> bool:
            return not self.container

        def push(self, item):
            self.container.append(item)

        def pop(self):
            return self.container.popleft()

        def __repr__(self) -> str:
            return repr(self.container)


    def bfs(start: T, end_condition: Callable[[T], bool], search_dom: Callable) -> None | Node:
        qe: Queue = Queue()
        first_node = Node(start, None)
        qe.push(first_node)

        explored: set[T] = {start}

        while not qe.is_empty:
            current_node: Node = qe.pop()
            current_content = current_node.current_content
            if end_condition(current_content):
                return current_node

            for child in search_dom(current_content):
                if child in explored:
                    continue
                qe.push(Node(child, current_node))
                explored.add(child)
        return None


    def path_to_print(node: Node) -> List[T]:
        path: List[T] = []
        while node is not None:
            path.append(node.current_content)
            node = node.parent_node
        path.reverse()
        return path


    # solution = bfs("Boston", lambda x: x == "Miami", city_graph.neighbors_of_vertex)
    # print(path_to_print(solution))