
N = 8

board = [-1] * N


def is_safe(row, col):

    for prev_row in range(row):

        prev_col = board[prev_row]

        if prev_col == col:
            return False

        if abs(prev_row - row) == abs(prev_col - col):
            return False

    return True


def solve(row):

    if row == N:
        return True

    for col in range(N):

        if is_safe(row, col):

            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False


def print_board():

    for row in range(N):

        for col in range(N):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


if solve(0):
    print("Solution found:")
    print_board()
else:
    print("No solution exists.")
