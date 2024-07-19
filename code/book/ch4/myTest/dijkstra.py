from __future__ import annotations
from dataclasses import dataclass
from weight_edge import WeightEdge
from weightgraph import WeightGraph
from priority_queue import PriorityQueue
from typing import List, Tuple, Dict, TypeVar, Optional


V = TypeVar('V')
@dataclass
class DijkstraNode:
    vertex: V
    distance: float

    def __lt__(self, other: DijkstraNode) -> bool:
        return self.distance < other.distance

    def __eq__(self, other: DijkstraNode) -> bool:
        return self.distance == other.distance



def dijkstra(wg: WeightGraph, start: V):
    first = DijkstraNode(start, 0)
    distances: Dict[V, float] = {start: 0}
    path_dict: Dict[V, WeightEdge] = {}

    pq: PriorityQueue = PriorityQueue()
    pq.push(first)

    while not pq.empty:
        current_node = pq.pop()
        distance = current_node.distance
        for edge in wg.edges_of_vertex(current_node.vertex):
            vertex = wg.vertex_at(edge.t)
            new_distance = distance + edge.weight
            if vertex not in distances or distances[vertex] > new_distance:
                distances[vertex] = new_distance
                path_dict[vertex] = edge
                pq.push(DijkstraNode(vertex, new_distance))
    return distances, path_dict

def distance_from_root(distances: Dict[V, float]):
    for v,d in distances.items():
        print(f"{v} -> {d}")

def print_dijkstra_path(wg:WeightGraph, start:V, end:V, path_dict: Dict[V, WeightEdge]):
    path: V = [end]
    weight: List[float] = []
    v = end
    while v != start:
        weight.append(path_dict[v].weight)
        v: V = wg.vertex_at(path_dict[v].f)
        path.append(v)
    path.reverse()
    weight.reverse()
    for i in range(len(weight)):
        print(f"{path[i]:<15} -> {path[i+1]:<15} cost {weight[i]:<}")
    print(f"Total weight: {sum(weight)}")


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

    distances_list, path_dicts = dijkstra(city_graph2, "Los Angeles")
    # distance_from_root(distances)
    print_dijkstra_path(city_graph2,"Los Angeles", "Philadelphia", path_dicts)

