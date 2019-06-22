from __future__ import annotations
from typing import TypeVar, Tuple, Type
from abc import abstractmethod, ABC

T = TypeVar("T", bound="Chromosome")  # return self? what?

# base class for all chromosomes. must override.
class Chromosome(ABC):
    @abstractmethod
    def fitness(self) -> float:
        pass

    @classmethod
    @abstractmethod
    def random_instance(cls: Type[T]) -> T:
        pass

    @abstractmethod
    def crossover(self: T, other: T) -> Tuple[T, T]:
        pass
    @abstractmethod
    def mutate(self) -> None:
        pass

