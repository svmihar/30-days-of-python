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

Point = TypeVar('Point', bound=DataPoint)

class KMeans(Generic[Point]): 
    @dataclass
    class cluster: 
        points: List[POINT]
        centroid: DataPoint

    def __init__(self, k, points) -> None: 
        if k<1: 
            raise ValueError('k must be >=1')
        self._points: List[Point] = points
        self._zscore_normalize()
        # initialize empty cluster with random k centroids
        self._clusters: List[KMeans.cluster] = []
        for _ in range(k): 
            rand_point: DataPoint = self._random_point()
            cluster: KMeans.cluster = KMeans.cluster([], rand_point)
            self._clusters.append(cluster)
    
    @property
    def _centroids(self) -> List[DataPoint]: 
        return [x.centroid for x in self._clusters]

    def _dimension_slice(self, dimension)-> List[float]: 
        # the hell is this for?
        return [x.dimensions[dimension] for x in self._points]
    
    def _zscore_normalize(self) -> None: 
        zscored: List[List[float]] = [[] for _ in range(len(self._points))]
        for dimension in range(self._points[0].num_dimensions): 
            dimension_slice: List[float] = self._dimension_slice(dimension)
            for index, zscore in enumerate(dimension_slice): 
                zscored[index].append(zscore)
        for i in range(self._points): 
            self._points[i].dimension = tuple(zscored[i])