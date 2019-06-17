from __future__ import annotations
from typing import TypeVar, List, Optional, Tuple, Dict
from dataclasses import dataclass
from mst import WeightedPath, print_weighted_path
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue

V = TypeVar('V')

@dataclass
class DijkstraNode: 
    vertex: int
    distance: float

    def __lt__(self, other: DijkstraNode) -> bool: 
        return self.distance < other.distance

    def __eq__(self, other: DijkstraNode) -> bool: 
        return self.distance == other.distance

def dijkstra(wg: WeightedEdge[V], root: V):
    first: int = wg.index_of(root) # find starting index, dari root, passed from parameter di atas bray 
    distances: List[Optional[float]] = [None] * wg.vertex_count
    distances[first] = 0 # distance dari root ke root ya 0 
    
    path_dict: Dict[int, WeightedEdge] = {} # yang save path nya dari current ke tujuan

    pq: PriorityQueue[DijkstraNode] = PriorityQueue()
    pq.push(DijkstraNode(first, 0)) # masukin current vertex / starting point 


    while not pq.empty: 
        u: int = pq.pop().vertex # explore the next closest vertex

        dist_u: float = distances[u]

        for we in wg.edges_for_index(u): 
            dist_v = distances[we.v]

            if dist_v is None or dist_v > we.weight + dist_u: 
                # update distance to this vertex
                distances[we.v] = we.weight + dist_u
                # update the edge on the shortest path to this vertex. 
                path_dict[we.v] = we

                # exlore it soon? 
                pq.push(DijkstraNode(we.v, we.weight + dist_u))

    return distances, path_dict

# helper function to print dijkstra results 
def distance_array_to_vertex_dict(wg: WeightedGraph[V], distances: List[Optional[float]]) -> Dict[V, Optional[float]]: 
    distance_dict: Dict[V, Optional[float]] = {}
    for i in range(len(distances)): 
        distance_dict[wg.vertex_at(i)] = distances[i]
    return distance_dict


# helper function that prints 'start' to 'end'
def path_dict_to_path(start: int, end: int, path_dict: Dict[int, WeightedEdge]) -> WeightedPath: 
    if len(path_dict) == 0: 
        return []
    edge_path: WeightedPath = []
    e: WeightedEdge = path_dict[end]
    edge_path.append(e)
    while e.u != start: 
        e = path_dict[e.u]
        edge_path.append(e)
    return list(reversed(edge_path))

if __name__ == "__main__":
    
    city_graph2: WeightedGraph[str] = WeightedGraph(["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston", "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])

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

    distances, path_dict = dijkstra(city_graph2, 'Los Angeles')
    name_distance = distance_array_to_vertex_dict(city_graph2, distances)
    
    print('Distances from Los Angeles to: ')
    for key, value in name_distance.items(): 
        print(f'{key}: {value}')
    print('')

    print('Shortest path from Los Angeles to Boston with path')
    print_weighted_path(path_dict_to_path(city_graph2.index_of('Los Angeles'), city_graph2.index_of('Boston'), path_dict))