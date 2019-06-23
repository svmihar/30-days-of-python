from __future__ import annotations
from typing import TypeVar, Generic, List, Sequence
from copy import deepcopy
from random import uniform
from statistics import mean, pstdev
from dataclasses import dataclass
from data_point import DataPoint


def zscores(original: Sequence[float]) -> List[float]:
    avg: float = mean(original)
    std: float = pstdev(original)

    if std == 0:  # return all zero, because no variation in list
        return [0] * len(original)
    return [(x - avg) / std for x in original]

POINT = TypeVar('Point', bound=DataPoint)

class KMeans(Generic[Point]): 
    @dataclass
    class cluster: 
        points: List[POINT]
        centroid: DataPoint

        
