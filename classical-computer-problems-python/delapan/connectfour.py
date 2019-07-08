#! ../.venv/bin/python
from __future__ import annotations
from typing import List, Optional, Tuple
from enum import Enum
from board import Piece, Board, Move

# SEJUJURNYA saya gak ngerti gimana cara main connect four dan terlalu males untuk googling. so we leave it here.


def generate_segments(num_columns: int, num_rows: int, segment_length: int) -> List[List[Tuple[int, int]]]:
    segments: List[List[Tuple[int, int]]] = []
    # generate vertical segments
    for c in range(num_columns):
        for r in range(num_rows - segment_length + 1):
            segment: List[Tuple[int, int]] = []
            for t in range(segment_length):
                segment.append((c, r+t))
            segments.append(segment)

    # generate horizontal
    for c in range(num_columns - segment_length + 1):
        for r in range(num_rows):
            segment = []
            for t in range(segment_length):
                segment.append((c+t, r))
            segments.append(segment)

    # generate the bottom left to top right diagonal segments
    for c in range(num_columns - segment_length + 1):
        for r in range(num_rows - segment_length + 1):
            segment = []
            for t in range(segment_length):
                segment.append((c + t, r + t))
            segments.append(segment)

    # generate top left to bottom right diagonal segments
    for c in range(num_columns - segment_length + 1):
        for r in range(segment_length - 1, num_rows):
            segment = []
            for t in range(segment_length):
                segment.append((c + t, r - t))
            segments.append(segment)
    return segments


class C4Piece(Piece, Enum):
    B = 'B'
    R = 'R'
    E = ' '

    @property
    def opposite(self) -> C4Piece:
        if self == C4Piece.B:
            return C4Piece.R
        elif self == C4Piece.R:
            return C4Piece.B
        else:
            return C4Piece.E

    def __str__(self) -> str:
        return self.value
# mirip bangt sama TTTPiece


class C4Board(Board):
    NUM_ROWS: int = 6
    NUM_COLUMNS: int = 7
    SEGMENT_LENGTH: int = 4

    class Column:
        def __init__(self) -> None:
            self._container: List[C4Piece] = []

        @property
        def full(self) -> bool:
            return len(self._container) == C4Board.NUM_ROWS

        def push(self, item) -> None:
            if self.full:
                raise OverflowError("lah udah penuh berak")
            self._container.append(item)

        def __getitem__(self, index: int) -> C4Piece:
            if index > len(self._container) - 1:
                return C4Piece.E
            return self._container[index]

        def __repr__(self) -> str:
            return repr(self._container)

        def copy(self) -> C4Board.Column:
            temp: C4Board.Column = C4Board.Column()
            temp._container = self._container.copy()
            return temp
    SEGMENTS: List[List[int, int]] = generate_segments(
        NUM_COLUMNS, NUM_ROWS, SEGMENT_LENGTH)

    def __init__(self, position: Optional[List[C4Board.Column]] = None, turn: C4Piece = C4Piece.B) -> None:
        if position is None: 
            self.position: List[C4Board.Column] = [C4Board.Column() for _ in range(C4Board.NUM_COLUMNS)]
        else: 
            self.position = position
        self._turn: C4Piece = turn
    
    @property
    def turn(self) -> Piece:
        return self._turn
    
    def move(self, location: Move) -> Board: 
        temp_position: List[C4Board.Column] = self.position.copy()
        for c in range(C4Board.NUM_COLUMNS): 
            temp_position[c] = self.position[c].copy()
        temp_position[location].push(self._turn)
        return C4Board(temp_position, self._turn.opposite)

    @property
    def legal_moves(self) -> List[Move]: 
        return [Move(c) for c in range(C4Board.NUM_COLUMNS) if not self.position[c].full]