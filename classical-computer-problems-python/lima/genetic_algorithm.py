from __future__ import annotations
from typing import TypeVar, Generic, List, Tuple, Callable
from enum import Enum
from random import choices, random
from heapq import nlargest
from statistics import mean

# from numpy import average
from chromosome import Chromosome

C = TypeVar("C", bound=Chromosome)


class GeneticAlgorithm(Generic[C]):
    SelectionType = Enum("SelectionType", "ROULETTE TOURNAMENT")

    def __init__(
        self,
        initial_population: List[C],
        threshold: float,
        max_generations: int = 100,
        mutation_chance: float = 0.01,
        crossover_chance: float = 0.7,
        selection_type=SelectionType.TOURNAMENT,
    ) -> None:
        self._population = initial_population
        self._threshold = threshold
        self._max_generations = max_generations
        self._mutation_chance = mutation_chance
        self._crossover_chance = crossover_chance
        self._fitness_key = type(self._population[0]).fitness
        self._selection_type = selection_type

    def _pick_roulette(self, wheel: List[float]) -> Tuple[C, C]:
        return tuple(choices(self._population, weights=wheel, k=2))

    def _pick_tournament(self, num_participants: int) -> Tuple[C, C]:
        participants: List = choices(self._population, k=num_participants)
        return tuple(
            nlargest(2, participants, key=self._fitness_key)
        )  # returns 2 largest fitness_key participant

    # it's reproducing time
    def _reproduce_and_replace(self) -> None:
        new_population: List[C] = []
        while len(new_population) < len(self._population):
            if self._selection_type == GeneticAlgorithm.SelectionType.ROULETTE:
                parents: Tuple[C] = self._pick_roulette(
                    [x.fitness() for x in self._population]
                )
            else:
                parents = self._pick_tournament(len(self._population) // 2)
            if random() < self._crossover_chance:
                new_population.extend(parents[0].crossover(parents[1]))
            else:
                new_population.extend(parents)
        # if odd number, remove the extra ones
        if len(new_population) > len(self._population):
            new_population.pop()
        self._population = new_population  # replace reference

    def _mutate(self) -> None:
        for individual in self._population:
            if random() < self._mutation_chance:
                individual.mutate()

    def run(self) -> C:
        best: C = max(self._population, key=self._fitness_key)
        for generation in range(self._max_generations):
            if best.fitness() >= self._threshold:
                print('called.')
                return best
            print(
                f"Generation {generation} Best {best.fitness()} Avg {mean(map(self._fitness_key, self._population))}"
            )
            self._reproduce_and_replace()
            self._mutate()
            highest: C = max(self._population, key=self._fitness_key)
            if highest.fitness() > best.fitness():
                best = highest  # replace with new best

        return best


if __name__ == "__main__":

    c = GeneticAlgorithm(initial_population=100, threshold=0.01)
    print(c.SelectionType)
