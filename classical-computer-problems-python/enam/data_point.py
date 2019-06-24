from __future__ import annotations
from typing import Iterator, List, Tuple, Iterable
# from numpy import sqrt
from math import sqrt 


class DataPoint:
    def __init__(self, initial: Iterable[float]) -> None:
        self._originals: Tuple[float, ...] = tuple(initial)
        self.dimensions: Tuple[float, ...] = tuple(initial)

    @property
    def num_dimensions(self) -> None:
        return len(self.dimensions)

    def distance(self, other: DataPoint) -> float:
        # Euclidean distance 
        combined: Iterator[Tuple[float, float]] = zip(self.dimensions, other.dimensions)

        differences: List[float] = [(x-y)**2 for x in combined]
        return sqrt(sum(differences))

    def __eq__(self, other: object) -> bool: 
        if not isinstance(other, DataPoint): 
            return NotImplemented
        return self.dimensions == other.dimensions

    def __repr__(self) -> str: 
        return self._originals.__repr__()
