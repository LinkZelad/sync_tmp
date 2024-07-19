from __future__ import annotations
from weightgraph import WeightGraph
from weight_edge import WeightEdge
from typing import List, Dict, Optional, TypeVar
from priority_queue import PriorityQueue

V = TypeVar('V')

def mini_spanning_tree(wg: WeightGraph, start: V):
    visited: Dict[V, bool] = {}
    for v in wg.vertices:
        visited[v] = False

    path: List[WeightEdge] = []
    pq: WeightEdge = PriorityQueue()

    def add_visit(v:V):
        visited[v] = True
        for edge in wg.edges_of_vertex(v):
            if visited[wg.vertex_at(edge.t)]:
                continue
            pq.push(edge)

    add_visit(start)

    while not pq.empty:
        current: WeightEdge = pq.pop()
        if visited[wg.vertex_at(current.t)]:
            continue
        path.append(current)
        add_visit(wg.vertex_at(current.t))
    return path

def total_weight(wp: WeightEdge):
    return sum(e.weight for e in wp)

def print_weighted_path(wg: WeightGraph, wp: List[WeightEdge]) -> None:
    for edge in wp:
        print(wg.vertex_at(edge.f), " -> ", wg.vertex_at(edge.t), " > ", edge.weight)
    print(f"Total Weight: {total_weight(wp)}")

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

    pa = mini_spanning_tree(city_graph2, "New York" )
    print_weighted_path(city_graph2, pa)