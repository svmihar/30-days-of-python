from __future__ import annotations
from typing import TypeVar, Generic, List, Sequence
from copy import deepcopy
from random import uniform
from statistics import mean, pstdev
from dataclasses import dataclass
from data_point import DataPoint

Point = TypeVar("Point", bound=DataPoint)


def zscores(original: Sequence[float]) -> List[float]:
    avg: float = mean(original)
    std: float = pstdev(original)

    if std == 0:  # return all zero, because no variation in list
        return [0] * len(original)
    return [(x - avg) / std for x in original]


class KMeans(Generic[Point]):
    @dataclass
    class cluster:
        points: List[POINT]
        centroid: DataPoint

    def __init__(self, k, points) -> None:
        if k < 1:
            raise ValueError("k must be >=1")
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

    def _dimension_slice(self, dimension) -> List[float]:
        # the hell is this for?
        return [x.dimensions[dimension] for x in self._points]

    def _zscore_normalize(self) -> None:
        zscored: List[List[float]] = [[] for _ in range(len(self._points))]
        for dimension in range(self._points[0].num_dimensions):
            dimension_slice: List[float] = self._dimension_slice(dimension)
            for index, zscore in enumerate(dimension_slice):
                zscored[index].append(zscore)
        for i in range(len(self._points)):
            self._points[i].dimension = tuple(zscored[i])

    def _random_point(self) -> DataPoint:
        rand_dimensions: List[float] = []
        for dimension in range(self._points[0].num_dimensions):
            values: List[float] = self._dimension_slice(dimension)
            rand_value: float = uniform(min(values), max(values))
            rand_dimensions.append(rand_value)
        return DataPoint(rand_dimensions)

    def _assign_clusters(self) -> None:
        for point in self._points:
            closest: DataPoint = min(
                self._centroids, key=partial(DataPoint.distance, point)
            )
            idx: int = self._centroids.index(closest)
            cluster: KMeans.cluster = self._clusters[idx]
            cluster.points.append(point)

    def _generate_centroids(self) -> None:
        # why can't we use dimension_slice?
        for cluster in self._clusters:
            if len(cluster.points) == 0:
                continue
            means: List[float] = []
            for dimension in range(cluster.points[0].num_dimensions):
                dimension_slice: List[float] = [
                    p.dimensions[dimension] for p in cluster.points
                ]
                means.append(mean(dimension_slice))
            cluster.centroid = DataPoint(means)

    def run(self, max_iterasion: int = 1000) -> List[KMeans.cluster]:
        for iterasi in range(max_iterasion):
            for cluster in self._clusters:
                cluster.points.clear()
            self._assign_clusters()
            old_centroids = deepcopy(self._centroids)
            self._generate_centroids()
            if old_centroids == self._centroids:
                print(f"Converged after {iterasi} iterations")
                return self._clusters
        return self._clusters


if __name__ == "__main__":
    point1: DataPoint = DataPoint([2.0, 1.0, 1.0])
    point2: DataPoint = DataPoint([2.0, 2.0, 5.0])
    point3: DataPoint = DataPoint([3.0, 1.5, 2.5])

    test = KMeans(2, [point1, point2, point3])
    clusters: List[KMeans.cluster] = test.run()
    for index, cluster in enumerate(clusters):
        print(f"CLuster {index}: {cluster.points}")

