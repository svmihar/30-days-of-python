"""
THIS IS ONLY A SCRATCHPAD SO I DON'T NEED TO BE SO TELITI ON MY WRITINGS, THE INTELLISENSE DOES THAT JOB FOR ME. 

I COPIED THE CODE TO JUPYTER LAB, USED PYTHON INTERACTIVE TO TEST IT IN VSCODE. 

ALL NOTES AND CATETAN WILL BE AT THE IPYNB FILE. 
"""

from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random 
from dua.generic_search import dfs, node_to_path, Node


class Cell(str, Enum): 
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    END = 'E'
    PATH = "*"

class MazeLocation(NamedTuple): 
    row: int
    column: int

class Maze: 
    def __init__(self, rows = 10, columns = 10, sparseness = 0.2, start = MazeLocation(0,0), end = MazeLocation(9,9)) :
        self._rows = rows
        self._columns = columns
        self.start = start
        self.end = end
        
        #fill grid with empty elements
        self._grid = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]

        #populate with blocked cells
        self._random_fill(rows, columns, sparseness)

        #fill the start and location 
        self._grid[start.row][start.column] = Cell.START
        self._grid[end.row][end.column] = Cell.END
    
    def _random_fill(self, rows, columns, sparseness): 
        for row in range(rows): 
            for column in range(columns):
                if random.uniform(0,1.0) < sparseness: 
                    self._grid[row][column] = Cell.BLOCKED
    
    def __str__(self): 
        output = ""
        for row in self._grid: 
            output += "".join([c.value for c in row]) + '\n' 
        return output

    def goal_test(self, ml): 
        return ml == self.end

    def successors(self, ml): 
        """
        Checks if the path is blocked or not by checking below, above, to the right and to the left of a maze, kalo ada kosong berarti bisa diisi, kalo gak ya berarti itu gak bisa. ya apa sih. 
        """
        locations: List[MazeLocation] = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED: 
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED: 
            locations.append(MazeLocation(ml.row-1, ml.column))
        if ml.column + 1 <self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED: 
            locations.append(MazeLocation(ml.row, ml.column+1))
        if ml.column -1 >= 0 and self._grid[ml.row][ml.column-1] != Cell.BLOCKED: 
            locations.append(MazeLocation(ml.row,ml.column-1))
        return locations

    def mark(self, path): 
        for maze_location in path: 
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.end.row][self.end.column] = Cell.END
    
    def clear(self, path): 
        for maze_location in path: 
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.end.row][self.end.column] = Cell.END
    
def manhattan_distance(goal: MazeLocation): 
    def distance(ml: MazeLocation): 
        xdist = abs(ml.column - goal.column)
        ydist = abs(ml.row - goal.row)
        return xdist-ydist
    return distance

from math import sqrt
def euclidean_distance(goal: MazeLocation): 
    def distance(ml: MazeLocation):
        x = ml.column - goal.column
        y = ml.row - goal.row
        return sqrt(x**2 + y**2)
    return distance


from dua.generic_search import bfs, astar

if __name__ == "__main__":   
    m = Maze()
    print(m)

    sol1,counter = dfs(m.start, m.goal_test, m.successors)
    print('-'*10)
    print('TESTING DFS')
    print('-'*10)
    if sol1 is None: 
        print('no solution from dfs')
    else: 
        print(f'used {counter} steps')
        path1 = node_to_path(sol1)
        m.mark(path1)
        print(m)
        m.clear(path1)
        # print(sol1.i)

    sol2 = bfs(m.start, m.goal_test, m.successors)
    print('-'*10)
    print('TESTING BFS ')
    print('-'*10)
    if sol2 is None: 
        print('no solution from bfs')
    else: 
        path2 = node_to_path(sol2)
        m.mark(path2)
        print(m)
        m.clear(path2)
        # print(sol2.i)
    
    
    ### TESTING A* ###
    distance = manhattan_distance(m.end)
    sol3 = astar(m.start, m.goal_test, m.successors, distance)
    print('-'*10)
    print('TESTING A*')
    print('-'*10)
    if sol3 is None: 
        print('no solution from a*')
    else: 
        path3 = node_to_path(sol3)
        m.mark(path3)
        print(m)
        m.clear(path3)
        # print(sol3.i)

    ### TESTING A* WITH EUCLIDEAN DISTANCE###
    distance = euclidean_distance(m.end)
    sol4 = astar(m.start, m.goal_test, m.successors, distance)
    print('-'*10)
    print('TESTING A* WITH EUCLIDEAN DISTANCE')
    print('-'*10)
    if sol4 is None: 
        print('no solution from a*')
    else: 
        path3 = node_to_path(sol4)
        m.mark(path3)
        print(m)
        m.clear(path3)
        # print(sol4.i)
