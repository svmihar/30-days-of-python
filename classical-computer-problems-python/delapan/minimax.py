from __future__ import annotations
from board import Piece, Board, Move

# find best possible outcome for original player
def minimax(board: Board, maximizing:bool, original_player: Piece, max_depth:int=8) -> float: 
    # best case, terminal position met
    if board.is_win or board.is_draw or max_depth== 0: 
        return board.evaluate(original_player)
    
    # recursive case, maximize gains aor minimize opponent gains
    if maximizing: 
        best_eval: float = float('-inf') # arbitrarily low starting value
        for move in board.legal_moves: 
            result: float = minimax(board.move(move), False, original_player, max_depth-1)
            best_eval = max(result, best_eval)
        return best_eval
    else: # minimizing
        worst_eval : float 
        for move in board.legal_moves:
            result= minimax(board.move(move), True, original_player, max_depth-1)
        worst_eval = min(result,worst_eval)
        return worst_eval
    # each recursive call keep tracks the board position, minimizing or maximizing and who we are trying to evaluate. and deal with best case scenario, terminal condition (Win, lose, draw)

    # find best possible move looking up to max-depth ahead.
    # dibuat karena minimax hanya evalute bool function.
    def find_best_move(board: Board, max_depth:int=8) -> Move: 
        best_eval:float = float('-inf')
        best_move: Move = Move(-1)
        for move in board.legal_moves: 
            result: float = minimax(board.move(move), False, board.turn, max_depth)
            if result > best_eval: 
                best_eval = result
                best_move = move
        return best_move

    