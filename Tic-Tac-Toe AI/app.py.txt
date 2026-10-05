import math


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]


def minimax(board, depth, is_maximizing):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r, c in get_available_moves(board):
            board[r][c] = "O"
            score = minimax(board, depth + 1, False)
            board[r][c] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r, c in get_available_moves(board):
            board[r][c] = "X"
            score = minimax(board, depth + 1, True)
            board[r][c] = " "
            best_score = min(score, best_score)
        return best_score


def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for r, c in get_available_moves(board):
        board[r][c] = "O"
        score = minimax(board, 0, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            move = (r, c)
    return move


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human turn
        r, c = -1, -1
        while (r, c) not in get_available_moves(board):
            try:
                move = input("Enter your move (row and column 0-2): ").split()
                r, c = int(move[0]), int(move[1])
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as two numbers (0-2).")

        board[r][c] = "X"
        print_board(board)

        if check_win(board, "X"):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        # AI turn
        print("AI is making a move...")
        ai_r, ai_c = best_move(board)
        board[ai_r][ai_c] = "O"
        print_board(board)

        if check_win(board, "O"):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break


if __name__ == "__main__":
    play_game()

