from csp import Constraint, CSP 
from typing import Dict, List, Optional 

class QueensConstraint(Constraint[int, int]): 
    def __init__(self, columns): 
        super().__init__(columns)
        self.columns = columns

    def satisfied(self, assignment) -> bool: 
        for q1c, q1r in assignment.items(): 
            for q2c in range(q1c+1,  len(Self.columns)+1): 
                if q2c in assignment: 
                    q2r :int = assignment[q2c]
                    if q1r == q2r: 
                        return False 
                    if abs(q1r - q2r) == abs(q1c - q2c): 
                        return False 
        return True


if __name__ == "__main__":
    columns = [x for x in range(1,9)]
    rows = {}
    for column in columns: 
        rows[column] = [x for x in range(1,9)]
    csp: CSP[int, int]=CSP(columns, rows)

    csp.add_constraint(QueensConstraint(columns))
    solution = csp.backtracking_search()
    if solution is None: 
        print('no solution')
    else: 
        print(solution)