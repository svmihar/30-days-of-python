from typing import TypeVar, Generic, Optional, List
from edge import Edge

V = TypeVar('V')

class Graph(Generic[V]): 
    def __init__(self, vertices: List[V] = []) -> None: 
        self._vertices: List[V] = vertices
        self._edges : List[List[Edge]] = [[] for _ in vertices] # adjacency list

    def vertex_count(self) -> int: 
        pass
    
    def add_vertex(self, vertex: V)-> int: 
        pass

    def add_edge(self, edge: Edge) -> None: 
        pass

    def add_edge_by_indices(self, u: int, v: int) -> None: 
        pass

    def add_edge_by_vertices(self, first: V, second: V) -> None: 
        pass

    def vertex_at(self, index: int) -> V: 
        pass
    
    def index_of(self, vertex: V): 
        pass

    def neighbors_for_index(self, index: int) -> List[V]: 
        pass

    def neighbors_for_vertex(self, vertex: V) -> List[V]: 
        pass

    def edges_for_index(self, index:int)->List[Edge]: 
        pass 

    def edges_for_vertex(self, vertex: V)->List[Edge]: 
        pass

    def __str__(self) -> str: 
        desc: str=""
        for i in range(self.vertex_count): 
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}"
        return desc
    