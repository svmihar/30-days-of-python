from typing import TypeVar, Generic, List
from heapq import heappush, heappop

T = TypeVar('V')

class PriorityQueue(Generic[T]): 
    def __init__(self): 
        self._container: List[T] = []

    def push(self, item: T): 
        heappush(self._container, item) # in by priority

    def pop(self, item: T): 
        return heappop(self._container) # out by priority
    
    def __repr__(str): 
        return(repr(self._container))