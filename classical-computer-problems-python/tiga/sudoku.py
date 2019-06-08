import sys

def read():
    board = []
    for i, line in enumerate(sys.stdin):
        print(f'insert line {i}: ')
        row = []
        for cell in line[:9]:
            if cell == ".":
                row.append(0)
            else:
                row.append(int(cell))
        board.append(row)
    return board

def print_board(board):
    for row in board:
        for cell in row:
            if cell == 0:
                print("_", end=" ")
            else:
                print(cell, end=" ")

        print()

def guess(board, x, y):
    invalid = set()
    sx, sy = x // 3, y // 3
    for i in range(9):
        if board[y][i] > 0:
            invalid.add(board[y][i])

        if board[i][x] > 0:
            invalid.add(board[i][x])

        cx, cy = i // 3 + sx * 3, i % 3 + sy * 3
        if board[cy][cx] > 0:
            invalid.add(board[cy][cx])

    possible = set(range(1, 10)) - invalid
    return possible

def next(x, y):
    if x == 8:
        return 0, y+1
    else:
        return x+1, y

def solve(board, x, y, step):
    if step == 9 ** 2:
        return True

    nx, ny = next(x, y)

    if board[y][x] != 0:
        return solve(board, nx, ny, step+1)

    guesses = guess(board, x, y)
    for value in guesses:
        board[y][x] = value
        if solve(board, nx, ny, step+1):
            return True
    board[y][x] = 0
    return False

board = read()
solve(board, 0, 0, 0)
print_board(board, True)