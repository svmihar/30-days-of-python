from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar("V")
D = TypeVar("D")


class Constraint(Generic[V, D], ABC):
    def __init__(self):
        self.variables = variables

    @abstractmethod  # artinya harus di override sama subclassnya
    def satisfied(self, assignment):
        pass


class CSP(Generic[V, D]):
    def __init__(self, variables, domains) -> None:
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        for variable in self.variables:
            self.constraint[variable] = []
            if variable not in self.domains:
                raise LookupError(
                    'Every variables should have a domain assigned to it')

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError('Variable constraint not in CSP')
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in csp but not in assignment
        unassigned: List[V] = [
            v for v in self.variables if v not in assignment]

        # get every possible value in first unassigned value
        first: V = unassigned[0]
        for value in self.domains[first]:
            local = assignment.copy()
            local[first] = value
            # if still consistent we continue
            if self.consistent(first, local):
                result: Optional(Dict[V, D]) = self.backtracking_search(local)
                if result is not None:
                    return result
        return None
