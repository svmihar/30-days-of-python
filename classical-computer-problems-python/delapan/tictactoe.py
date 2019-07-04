from __future__ import annotations
from typing import List
from enum import Enum
from board import Piece, Board, Move


class TTTPiece(Piece, Enum):
    X = 'X'
    O = 'O'
    E = " "  # empty state

    @property
    def opposite(self) -> TTTPiece:
        if self == TTTPiece.X:
            return TTTPiece.O
        elif self == TTTPiece.O:
            return TTTPiece.X
        else:
            return TTTPiece.E


def __str__(self) -> str:
    return self.value


class TTTBoard(Board):
    def __init__(Self, position: List[TTTPiece] = [TTTPiece.E]*9, turn: TTTPiece = TTTPiece.X) -> None:
        self.position: List[TTTPiece] = position
        self._turn: TTTPiece = turn

    @property
    def turn(self) -> Piece:
        # ada 2 turn, dan _turn biar tiap board tau siapa giliran siapa. which membingungkan. w
        return self._turn
    

    def move(self, location: Move) -> Board: 
        # check all possible move without "switch turns", jadi state dimana dia di turn itu aja. 
        temp_position: List[TTTPiece] = self.position.copy()
        temp_position[location] = self._turn
        return TTTBoard(temp_position, self._turn.opposite)
    
    @property
    def legal_moves(self) -> bool: 
        # 3 row, 3 column and 2 diagonal check. 
        return self.position[0] == self.position[1] and self.position[0] == self.position[2] and self.position[0] != TTTPiece.E or self.position[3] == self.position[4] and self.position[3] == self.position[5] and self.position[3] !=TTTPiece.E or self.position[6]  == self.position[7] and self.position[6] == self.position[8] and self.position[6] != TTTPiece.E or self.position[1] == self.position[4] and self.position[1] == self.position[7] and self.position[1] != TTTPiece.E or self.position[2] == self.position[5] and self.position[2] ==self.position[8] and self.position[2] != TTTPiece.E or self.position[0] == self.position[4] and self.position[0] == self.position[8] and self.position[0] != TTTPiece.E or self.position[2] == self.position[4] and self.position[2] == self.position[6] and self.position[2] != TTTPiece.E