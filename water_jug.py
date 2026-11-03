
JUG_A = 4
JUG_B = 3

GOAL = 2


def get_next_states(a, b):
    states = []

    states.append((JUG_A, b))

    states.append((a, JUG_B))

    states.append((0, b))

    states.append((a, 0))

    amount = min(a, JUG_B - b)
    states.append((a - amount, b + amount))

    amount = min(b, JUG_A - a)
    states.append((a + amount, b - amount))

    return states


def dfs():
    start = (0, 0)

    stack = [start]

    visited = {start}

    parent = {start: None}

    while stack:

        current = stack.pop()

        a, b = current

        if a == GOAL or b == GOAL:
            return parent, current

        for next_state in get_next_states(a, b):

            if next_state not in visited:
                visited.add(next_state)

                parent[next_state] = current

                stack.append(next_state)

    return None, None


def print_solution(parent, goal_state):

    if goal_state is None:
        print("No solution exists.")
        return

    path = []
    current = goal_state

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Solution Path:")

    for state in path:
        print(state)


parent, goal_state = dfs()

print_solution(parent, goal_state)
