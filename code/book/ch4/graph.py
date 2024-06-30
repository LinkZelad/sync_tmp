from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar("V")

class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)
    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))

    @property
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    @property
    def add_edge(self, edge: Edge):
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)