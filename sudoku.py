
def get_candidates(grid, row, col):
    # Find all valid numbers for an empty cell
    candidates = set(range(1, 10))

    # Remove numbers already present in the row
    for c in range(9):
        candidates.discard(grid[row][c])

    # Remove numbers already present in the column
    for r in range(9):
        candidates.discard(grid[r][col])

    # Find the top-left corner of the 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    # Remove numbers already present in the box
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            candidates.discard(grid[r][c])

    return candidates


def propagate(grid):
    # Keep applying constraints until no forced value remains
    while True:
        changed = False

        for row in range(9):
            for col in range(9):

                # Skip cells that are already filled
                if grid[row][col] != 0:
                    continue

                candidates = get_candidates(grid, row, col)

                # No possible number means contradiction
                if len(candidates) == 0:
                    return False

                # Only one possible number: fill it
                if len(candidates) == 1:
                    grid[row][col] = candidates.pop()
                    changed = True

        # If nothing changed, propagation is complete
        if not changed:
            return True


def solve(grid):
    # Apply constraint propagation first
    if not propagate(grid):
        return False

    # Find the empty cell with the fewest candidates
    best_cell = None
    best_candidates = None

    for row in range(9):
        for col in range(9):

            if grid[row][col] == 0:
                candidates = get_candidates(grid, row, col)

                if best_candidates is None or len(candidates) < len(best_candidates):
                    best_cell = (row, col)
                    best_candidates = candidates

    # No empty cells means the puzzle is solved
    if best_cell is None:
        return True

    row, col = best_cell

    # Try every possible number
    for number in best_candidates:

        # Save the current grid before making a guess
        old_grid = [r[:] for r in grid]

        grid[row][col] = number

        # Recursively solve the remaining puzzle
        if solve(grid):
            return True

        # Guess was incorrect: restore the previous grid
        for r in range(9):
            grid[r] = old_grid[r]

    return False


def print_grid(grid):
    for row in grid:
        print(row)


# Example Sudoku puzzle
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve(grid):
    print("Sudoku Solved:")
    print_grid(grid)
else:
    print("No solution exists.")
