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
    def __init__(self, position: List[TTTPiece] = [TTTPiece.E]*9, turn: TTTPiece = TTTPiece.X) -> None:
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
    def is_win(self) -> bool:
        # initinya mencari kalo kolom, baris atau diagonal nya tidak kosong dan mempunyai isi yang sama ya berarti gamenya menang.
        # gamenya drawn kalo tidak menang dan tidak ada lagi legal moves nya. dan sudah di cover di class boardnya.
        # 3 row, 3 column and 2 diagonal check.
        return self.position[0] == self.position[1] and self.position[0] == self.position[2] and self.position[0] != TTTPiece.E or self.position[3] == self.position[4] and self.position[3] == self.position[5] and self.position[3] != TTTPiece.E or self.position[6] == self.position[7] and self.position[6] == self.position[8] and self.position[6] != TTTPiece.E or self.position[1] == self.position[4] and self.position[1] == self.position[7] and self.position[1] != TTTPiece.E or self.position[2] == self.position[5] and self.position[2] == self.position[8] and self.position[2] != TTTPiece.E or self.position[0] == self.position[4] and self.position[0] == self.position[8] and self.position[0] != TTTPiece.E or self.position[2] == self.position[4] and self.position[2] == self.position[6] and self.position[2] != TTTPiece.E

    @property
    def legal_moves(self) -> List[Move]:
        return [Move(l) for l in range(len(self.position)) if self.position[l] == TTTPiece.E]

    def is_draw(self) -> bool: 
        return (not self.is_win) and (len(self.legal_moves) == 0)

    def evaluate(self, player: Piece) -> float:
        if self.is_win and self.turn == player:
            return -1
        elif self.is_win and self.turn != player:
            return 1
        else:
            return 0

    def __repr__(self) -> str:
        return f"""{self.position[0]} | {self.position[1]} | {self.position[2]}
        {self.position[3]} | {self.position[4]} | {self.position[5]} 
        {self.position[6]} | {self.position[7]} | {self.position[8]}"""