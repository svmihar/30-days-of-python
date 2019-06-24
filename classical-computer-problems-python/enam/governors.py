from __future__ import annotations
from typing import List
from data_point import DataPoint
from kmeans import KMeans


class Governor(DataPoint):
    def __init__(self, longitude: float, age: float, state: str) -> None:
        super().__init__([longitude, age])
        self.longitude = longitude
        self.age = age
        self.state = state

    def __repr__(self) -> str:
        return f"{self.state}: (longitude: {longitude}, age: {self.age})"

if __name__ == "__main__":
    pass