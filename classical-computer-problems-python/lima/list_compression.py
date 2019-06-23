from __future__ import annotations
from typing import Tuple, List, Any
from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm
from random import choices, sample, shuffle
from copy import deepcopy
from zlib import compress
from sys import getsizeof
from pickle import dumps

PEOPLE: List[str] = ['SUMIHAR', 'CHRISTIAN', 'NATHANAEL', 'SIAHAAN']

class ListCompression(Chromosome): 
    def __init__(self, lst): 
        self.lst = lst

    @property
    def bytes_compressed(self) -> int: 
        return getsizeof(compress(dumps(self.lst)))
    
    def fitness(self): 
        return 1 / self.bytes_compressed

    @classmethod
    def random_instance(cls) -> ListCompression: 
        myLst = deepcopy(PEOPLE)
        shuffle(myLst)
        return ListCompression(myLst)

    def crossover(self, other): 
        child1 = deepcopy(self)
        child2 = deepcopy(other)
        idx1, idx2 = sample(range(len(self.lst)), k=2)
        l1, l2 = child1.lst[idx1], child2.lst[idx2]
        child1.lst[child1.lst.index(l2)], child1.lst[idx2] = child1.lst[idx2], l2
        child2.lst[child2.lst.index(l1)], child2.lst[idx1] = child2.lst[idx1], l1
        return child1, child2 

    def mutate(self) -> None: # swap 2 locations 
        idx1, idx2 = sample(range(len(self.lst)), k=2)
        self.lst[idx1], self.lst[idx2] = self.lst[idx2], self.lst[idx1]

    def __str__(self) -> str: 
        return f"Order: {self.lst} Bytes: {self.bytes_compressed}"
