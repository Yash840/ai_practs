
from collections import deque

# Environment
grid = [
    ["S", ".", "#", "."],
    [".", ".", "#", "."],
    ["#", ".", ".", "."],
    [".", "#", ".", "G"]
]

start = (0, 0)
goal = (3, 3)

internal_state = {
    "position": start,
    "visited": set(),
    "model": grid
}


def find_path(model, start, goal):
    queue = deque([(start, [])])
    visited = {start}

    directions = [
        (1, 0),   # Down
        (-1, 0),  # Up
        (0, 1),   # Right
        (0, -1)   # Left
    ]

    rows = len(model)
    cols = len(model[0])

    while queue:
        position, path = queue.popleft()

        if position == goal:
            return path

        r, c = position

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            next_position = (nr, nc)

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue

            if model[nr][nc] == "#" or next_position in visited:
                continue

            visited.add(next_position)
            queue.append((next_position, path + [next_position]))

    return None

path = find_path(
    internal_state["model"],
    internal_state["position"],
    goal
)

if path:
    for next_position in path:
        internal_state["visited"].add(internal_state["position"])
        internal_state["position"] = next_position
        print("Agent moves to:", next_position)

    print("Goal reached!")
else:
    print("No path found!")
