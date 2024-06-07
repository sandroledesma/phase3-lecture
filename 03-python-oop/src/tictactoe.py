def print_board(board):
    print("  0   1   2")
    for i in range(len(board)):
        print(f"{i} " + " | ".join(board[i]))
        if i < len(board) - 1:
            print("  " + "-" * 9)

def check_win(board, player):
    # Check rows, columns and diagonals for a win
    win_conditions = (
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    )
    return [player, player, player] in win_conditions

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter_the_row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter_the_column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("This position is already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()