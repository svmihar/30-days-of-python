from empat.weighted_edge import WeightedEdge
from empat.graph import Graph
from typing import TypeVar, Generic, List, Tuple

V = TypeVar('V')
class WeightedGraph(Generic[V], Graph[V]): 
    def __init__(Self, vertices = []) -> None: 
        self._vertices: List[V] = vertices
        self._edges: List[V] = [ [] for _ in vertices]

    def add_edge_by_indices(self, u, v, weight: float) -> None: 
        edge: WeightedEdge = WeightedEdge(u,v, weight)
        self.add_edge(edge) # superclass version 

    def add_edge_by_vertices(self, first: V, second: V, weight: float) -> None: 
        u, v = self._vertices.index(first), self._vertices.index(second)
        self.add_edge_by_indices(u,v,weight)

    def neighbors_for_index_with_weights(self, index: int) -> List[Tuple[V, float]]: 
        distance_tuples: List[Tuple[V, float]] = []
        for edge in self.edges_for_index(index): 
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))
        return distance_tuples

    def __str__(self): 
        dec: str = ''
        for i in range(self.vertex_count): 
            dec+=f'{self.vertex_at(i)} --> {self.neighbors_for_index_with_weights(i)}\n'
        return dec