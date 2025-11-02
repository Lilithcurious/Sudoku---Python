# utils.py
def print_board(board):
    print("\n" + "╔" + "═" * 25 + "╗")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("╠" + "═" * 25 + "╣")
        row = "║ "
        for j in range(9):
            if board[i][j] == 0:
                row += ". "
            else:
                row += str(board[i][j]) + " "
            if (j + 1) % 3 == 0 and j != 8:
                row += "│ "
        row += "║"
        print(row)
    print("╚" + "═" * 25 + "╝\n")


def is_valid_move(board, row, col, num):
    temp = board[row][col]
    board[row][col] = num
    from sudoku_solver import is_valid
    valid = is_valid(board, row, col, num)
    board[row][col] = temp
    return valid