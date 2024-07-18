from __future__ import annotations

from typing import (List, Dict, TypeVar)

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

    def index_of_vertex(self, v:V) -> V:
        return self.vertices.index(v)

    def neighbors_of_index(self, f_index: int) -> List[V]:
        return [self.vertex_at(e.t) for e in self.edges[f_index]]

    def neighbors_of_vertex(self, v: V) -> List[V]:
        return self.neighbors_of_index(self.index_of_vertex(v))

    def edges_of_index(self, index: int) -> List[Edge]:
        return self.edges[index]

    def edges_of_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_of_index(self.index_of_vertex(vertex))

    def __str__(self):
        desc: str = ""
        desc += f"Vertices: {self.vertices}\n"
        desc += f"Vertex count: {self.vertex_count}\n"
        desc += "Edges:\n\033[31m"
        for v in self.vertices:
            desc += f"    {v} --> {[self.vertex_at(e.t) for e in self.edges[self.index_of_vertex(v)]]}\n"
        desc += "\033[0m"
        return desc


if __name__ == '__main__':
    g = Graph(["a", "b", "c", "d", "e"])
    g.add_edge_by_vertices("a", "b")
    g.add_edge_by_vertices("a", "e")
    g.add_edge_by_vertices("a", "d")
    print(g)
