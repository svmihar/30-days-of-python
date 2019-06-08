from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint
from pprint import pprint 


Grid = List[List[str]]  # type alias doang

class GridLocation(NamedTuple): 
    row: int
    column: int

def generate(rows, columns) -> Grid :
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)] 

def disp(grid: Grid) -> Grid: 
    for row in grid: 
        print("".join(row))

def generate_domain(word: str, grid: Grid) -> List[List[GridLocation]]: 
    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0])
    length: int = len(word)

    for row in range(height): 
        for col in range(width): 
            columns: range = range(col, col+length+1)
            rows: range = range(row, row+length+1)
            if col + length <= width: 
                # test dari kiri ke kanannya
                domain.append([GridLocation(row, c) for c in columns])
                # diagonal bawah kanan 
                if row + length <= height: 
                    domain.append([GridLocation(r, col + (r-row)) for r in rows])

            if row + length <= height: 
                # ATAS KE BAWAH
                domain.append([GridLocation(r, col) for r in rows])
                # diaganal bawah kiri 
                if col - length >= 0: 
                    domain.append([GridLocation(r, col - (r - row)) for r in rows])

    return domain


class WordSearchContraint(Constraint[str, List[GridLocation]]): 
    def __init__(self, words: List[str]) -> None: 
        super().__init__(words)
        self.words = words

    def satisfied(self, assignment: Dict[str, List[GridLocation]]) -> bool: 
        all_locations = [locs for values in assignment.values() for locs in values]
        print(all_locations)
        return len(set(all_locations)) == len(all_locations)



if __name__ == "__main__":
    grid: Grid = generate(9,9)
    words: List[str]= ['KEZIA', 'MARANNU', 'BIRING', 'SUMIHAR', 'CHRISTIAN']
    locations: Dict[str, List[List[GridLocation]]] = {}
    for word in words: 
        locations[word] = generate_domain(word, grid)
    print(locations)
    
    csp=CSP(words, locations)
    csp.add_constraint(WordSearchContraint(words))
    solution = csp.backtracking_search()

    if solution is None: 
        print('No solution found')
    else: 
        for word, grid_location in solution.items(): 
            if choice([True, False]): 
                grid_location.reverse()

            for index, letter in enumerate(word): 
                (row, col) = (grid_location[index].row, grid_location[index].column)
                grid[row][col] = letter
            disp(grid)