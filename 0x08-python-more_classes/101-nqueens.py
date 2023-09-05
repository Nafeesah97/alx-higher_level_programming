#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    # Check if it's safe to place a queen at board[row][col]

    # Check the column above
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False

    return True

def solve_nqueens(n):
    solutions = []

    def solve(row, board):
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1, board)

    solve(0, [-1] * n)
    return solutions

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)

    for solution in solutions:
        print([row for row in solution])

if __name__ == "__main__":
    main()
