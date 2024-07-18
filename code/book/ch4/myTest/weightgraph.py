from __future__ import annotations
from graph import Graph
from weight_edge import WeightEdge
from typing import TypeVar, List

V = TypeVar('V')

class WeightGraph(Graph):
    def __init__(self, vertices:List[V]=None):
        if vertices is None:
            vertices = []

        self.vertices: List[V] = vertices
        self.weight_edges: List[List[WeightEdge]] = []


    def add_edge_by_indices_with_weight(self, f_index: int, t_index: int, weight: float) -> bool:
        if f_index >= self.vertex_count or t_index >= self.vertex_count:
            print(f"The index must be in {self.vertex_count}!")
            return False
        edge = WeightEdge(f_index, t_index, weight)
        self.edges[f_index].append(edge)
        self.edges[t_index].append(edge.reversed())
        return True

    def add_edge_by_vertices_with_weight(self, f_v: V, t_v: V, weight: float) -> None:
        if f_v not in self.vertices:
            self.add_vertex(f_v)
        if t_v not in self.vertices:
            self.add_vertex(t_v)
        f_int = self.index_of_vertex(f_v)
        t_int = self.index_of_vertex(t_v)
        edge = WeightEdge(f_int, t_int, weight)
        self.add_edge(edge)


    def neighbors_of_index_with_weight(self, f_index: int) -> List[V]:
        return [self.vertex_at(e.t) for e in self.edges[f_index]]

    def neighbors_of_vertex_with_weight(self, v: V) -> List[V]:
        return self.neighbors_of_index(self.index_of_vertex(v))
