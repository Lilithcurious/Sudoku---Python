# main.py
from sudoku_generator import generate_sudoku
from utils import print_board, is_valid_move
from sudoku_solver import solve_sudoku
from copy import deepcopy

def main():
    print("Bem-vindo ao Sudoku!")
    board = generate_sudoku()
    original = deepcopy(board)

    print_board(board)

    while True:
        try:
            move = input("Digite 'linha coluna número' (ex: 1 2 5) ou 'sair': ").strip().lower()
            if move == "sair":
                print("Jogo encerrado.")
                break
            if move == "sol":
                print("Solução:")
                solve_sudoku(original)
                print_board(original)
                continue

            parts = move.split()
            if len(parts) != 3:
                print("Formato inválido! Use: linha coluna número")
                continue

            row = int(parts[0]) - 1
            col = int(parts[1]) - 1
            num = int(parts[2])

            if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
                print("Valores fora do intervalo! (1-9)")
                continue

            if original[row][col] != 0:
                print("Essa célula não pode ser alterada!")
                continue

            if not is_valid_move(board, row, col, num):
                print("Jogada inválida! Conflito na linha, coluna ou quadrante.")
                continue

            board[row][col] = num
            print_board(board)

            # Verifica vitória
            if all(board[i][j] != 0 for i in range(9) for j in range(9)):
                temp = deepcopy(board)
                if solve_sudoku(temp):
                    print("Parabéns! Você completou o Sudoku!")
                    break
                else:
                    print("Tabuleiro cheio, mas inválido. Continue corrigindo.")
        except:
            print("Entrada inválida. Tente novamente.")

if __name__ == "__main__":
    main()