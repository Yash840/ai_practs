
from collections import deque

def tower_of_hanoi(n):
    start = (tuple(range(n, 0, -1)), (), ())
    goal = ((), (), tuple(range(n, 0, -1)))

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            for move in path:
                print(move)
            print("Total moves:", len(path))
            return

        for i in range(3):
            if not state[i]:
                continue

            disk = state[i][-1]

            for j in range(3):
                if i == j:
                    continue

                if not state[j] or state[j][-1] > disk:
                    new_state = [list(rod) for rod in state]
                    new_state[i].pop()
                    new_state[j].append(disk)

                    new_state = tuple(tuple(rod) for rod in new_state)

                    if new_state not in visited:
                        visited.add(new_state)
                        new_path = path + [(f"Move disk {disk} from {chr(65+i)} to {chr(65+j)}")]
                        queue.append((new_state, new_path))

tower_of_hanoi(3)
