from __future__ import annotations
from typing import TypeVar, Generic, List, Tuple, Callable
from enum import Enum
from random import choices, random
from heapq import nlargest
from numpy import average
from chromosome import Chromosome

C = TypeVar('C', bound=Chromosome)

class GeneticAlgorithm(Generic[C]): 
    SelectionType = Enum('SelectionType', 'ROULETTE TOURNAMENT')

    def __init__(self, initial_population: List[C], threshold: float, max_generations: int = 100, mutation_chance: float = .01, crossover_chance: float = .7, selection_type = SelectionType.TOURNAMENT) -> None: 
        self._population = initial_population
        self._threshold = threshold
        self._max_generations = max_generations
        self._mutation_chance = mutation_chance
        self._crossover_chance = crossover_chance
        # self._fitness_key = type(self._population[0]).fitness
        self._selection_type = selection_type



if __name__ == "__main__":
    
    c = GeneticAlgorithm(initial_population=100, threshold=.01)
    print(c.SelectionType)