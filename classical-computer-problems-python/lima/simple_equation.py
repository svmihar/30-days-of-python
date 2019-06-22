from __future__ import annotations
from typing import Tuple, List 
from chromosome import Chromosome
from random import randrange, random 
from genetic_algorithm import GeneticAlgorithm
from copy import deepcopy

class SimpleEquation(Chromosome): 
    def __init__(self, x, y)-> None: 
        self.x: int = x 
        self.y: int = y 

    def fitness(self) -> float: 
        # 6x - x^2 + 4y - y^2
        return 6 * self.x - self.x**2 +  4 * self.y - self.y**2
    
    @classmethod
    def random_instance(cls) -> SimpleEquation:
        return SimpleEquation(randrange(100), randrange(100)) 
    
    def crossover(self, other: SimpleEquation) -> Tuple(SimpleEquation, SimpleEquation): 
        child1 : SimpleEquation = deepcopy(self)
        child2: SimpleEquation = deepcopy(other)
        child1.y = other.y 
        child2.y = self.y 

        return child1, child2

    def mutate(self) -> None: 
        if random() > .5: # mutate the x 
            if random() > .5: 
                self.x+=1
            else: 
                self.x-=1

        else: # otherwise mutate y 
            if random() > .5: 
                self.y+=1
            else: 
                self.y -=1

    def __str__(self) -> str: 
        return f'X: {self.x} Y: {self.y} Fitness: {self.fitness()}'

if __name__ == "__main__":
    initial_population : List[SimpleEquation] = [SimpleEquation.random_instance() for _ in range(20)]

    print(initial_population)

    ga: GeneticAlgorithm[SimpleEquation] = GeneticAlgorithm(initial_population, threshold=13.0, max_generations=100, mutation_chance=.1, crossover_chance=.7)
    result: SimpleEquation = ga.run()
    print(result)
