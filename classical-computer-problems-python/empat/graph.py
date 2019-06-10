from typing import TypeVar, Generic, Optional, List
from edge import Edge

V = TypeVar('V')

class Graph(Generic[V]): 
    def __init__(self, vertices: List[V] = []) -> None: 
        self._vertices: List[V] = vertices
        self._edges : List[List[Edge]] = [[] for _ in vertices] # adjacency list

    @property
    def edge_count(self) -> int: 
        return sum(map(len, self_.edges))

    def add_edge(self, edge: Edge) -> None: 
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u: int, v: int) -> None: 
        edge: Edge = Edge(u,v)
        self.add_edge(edge)

    def vertex_count(self) -> int: 
        return len(self._vertices)
    
    def add_vertex(self, vertex: V)-> int: 
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count-1

    def add_edge_by_vertices(self, first: V, second: V) -> None: 
        v, u = self._vertices.index[first], self._vertices[second]
        self.add_edge_by_indices(u,v)

    def vertex_at(self, index: int) -> V: 
        return self._vertices[index]
    
    def index_of(self, vertex: V): 
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index: int) -> List[V]: 
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbors_for_vertex(self, vertex: V) -> List[V]: 
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self, index:int)->List[Edge]: 
        return self._edges[index] 

    def edges_for_vertex(self, vertex: V)->List[Edge]: 
        return self.edges_for_index(self.index_of(vertex))

    def __str__(self) -> str: 
        desc: str=""
        for i in range(self.vertex_count): 
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}"
        return desc
    