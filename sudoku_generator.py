# sudoku_generator.py
import random
from copy import deepcopy
from sudoku_solver import solve_sudoku

def generate_sudoku():
    # Cria tabuleiro vazio
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Preenche diagonal (3 quadrantes 3x3) para garantir solução
    for box in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        idx = 0
        for i in range(3):
            for j in range(3):
                board[box + i][box + j] = nums[idx]
                idx += 1

    # Resolve o tabuleiro completo
    solve_sudoku(board)

    # Remove números para criar o puzzle (dificuldade média: ~40 removidos)
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    for _ in range(40):  # Remove 40 números
        row, col = positions.pop()
        board[row][col] = 0

    return board