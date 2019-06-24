from __future__ import annotations
from typing import List
from data_point import DataPoint
from kmeans import KMeans

class Album(DataPoint): 
    def __init__(self, name: str, year: int , length: float, tracks: float) -> None: 
        super().__init__([length, tracks])
        self.name = name
        self.year = year
        self.tracks = tracks

    def __repr__(self) -> str: 
        return f'{self.name}, {self.year}'

    if __name__ == "__main__":
        pass