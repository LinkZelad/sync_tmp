from __future__ import annotations
from dataclasses import dataclass
from mst import WeightedPath, print_weighted_path
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue
from typing import List, Tuple, Dict, TypeVar, Optional

V = TypeVar('V')


@dataclass
class DijkstraNode:
    vertext: int
    distance: float
    def __lt__(self, other: DijkstraNode) -> bool:
        return self.distance < other.distance

    def __eq__(self, other:DijkstraNode) -> bool:
        return self.distance == other.distance

def dijkstra(wg: WeightedGraph[V], root: V) -> Tuple[List[Optional[float]], Dict[int, WeightedEdge]]:
    first: int = wg.index_of_vertex(root)
    path_dict: Dict[int, WeightedEdge] = {}
    distances: List[Optional[float]] = [None] * wg.vertex_count
    distances[first] = 0

    pq: PriorityQueue = PriorityQueue()
    pq.push(DijkstraNode(first, 0))

    while not pq.empty():
        current: int = pq.pop().vertex
        dist_current: float = distances[current]

        for edge in wg.edges_for_index(current):
            dist_next: float = distances[edge.v]
            if dist_next is None or dist_next > edge.weight + dist_current:
                distances[edge.v] = edge.weight + dist_current
                path_dict[edge.v] = edge
                pq.push[DijkstraNode(edge.v, distances[edge.v] + dist_current)]

    return distances, path_dict

def distance_array_to_vertex_dict(wg: WeightedGraph[V], distances: List[Optional[float]]) -> Dict[V, Optional[float]]:
    distance_dict: Dict[V, Optional[float]] = {}
    for i in range(len(distances)):
        distance_dict[wg.vertex_at(i)] = distances[i]
    return distance_dict

def path_dict_to_path(start:int, end:int, path_dict: Dict[int, WeightedEdge]) -> WeightedPath:
    path: WeightedPath = []
    current: int = end
    while current != start:
        edge: WeightedEdge = path_dict[current]
        path.append(edge)
        current = edge.u
    path.reverse()
    return path

