from __future import annotations
from typing import List, Optional, Tuple
from enum import Enum
from board imoprt Piece, Board, Move 

class C4Piece(Piece, Enum): 
    B = 'B'
    R = 'R'
    E = ' '

    @property
    def opposite(self) -> C4Piece: 
        if self == C4Piece.B: 
            return C4Piece.R
        elif self== C4Piece.R: 
            return C4Piece.B
        else: 
            return C4Piece.E
    
    def __str__(self) -> str: 
        return self.value
# mirip bangt sama TTTPiece 

    def generate_segments(num_columns: int, num_rows: int, segment_length: int) -> List[List[Tuple[int, int]]]: 
        segments: List[List[Tuple[int, int]]]
        # generate vertical segments
        for c in range(num_columns): 
            for r in range(num_rows - segment_length + 1): 
                segment: List[Tuple[int, int]] = []
                for t in range(segment_length): 
                    segment.append((c,r+t))
                segments.append(segment)
        
        # generate horizontal 
        for c in range(num_columns- segment_length + 1): 
            for r in range(num_rows): 
                segment = []
                for t in range(segment_length): 
                    segment.append(c+t, r)
                segments.append(segment)
            