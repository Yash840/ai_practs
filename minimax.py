board = [" "] * 9

def check_winner():
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


def evaluate():
    winner = check_winner()

    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    elif " " not in board:
        return 0

    return None


def minimax(is_maximizing):
    score = evaluate()

    if score is not None:
        return score

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def best_move():
    best_score = -float("inf")
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


def display_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
        if i < 6:
            print("---------")
    print()


while True:
    move = best_move()
    board[move] = "X"

    print("AI plays:")
    display_board()

    result = evaluate()

    if result is not None:
        break

    human_move = int(input("Enter position (0-8): "))

    if human_move < 0 or human_move > 8 or board[human_move] != " ":
        print("Invalid move! Try again.")
        board[move] = " "
        continue

    board[human_move] = "O"

    print("Human plays:")
    display_board()

    result = evaluate()

    if result is not None:
        break

if result == 1:
    print("AI wins!")
elif result == -1:
    print("Human wins!")
else:
    print("Game Draw!")
