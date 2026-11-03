from collections import deque

GOAL_STATE = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

ACTIONS = {
    "UP":    (-1,  0),
    "DOWN":  ( 1,  0),
    "LEFT":  ( 0, -1),
    "RIGHT": ( 0,  1),
}


def get_successors(state):
    successors = []
    blank_idx = state.index(0)
    blank_r, blank_c = divmod(blank_idx, 3)

    for action_name, (dr, dc) in ACTIONS.items():
        new_r, new_c = blank_r + dr, blank_c + dc

        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_idx = new_r * 3 + new_c
            
            state_list = list(state)
            state_list[blank_idx], state_list[new_idx] = state_list[new_idx], state_list[blank_idx]
            next_state = tuple(state_list)
            
            successors.append((next_state, action_name))

    return successors


def solve_bfs(initial_state, goal_state=GOAL_STATE):
    if initial_state == goal_state:
        return []

    frontier = deque([(initial_state, [])])
    
    explored = {initial_state}

    nodes_expanded = 0

    while frontier:
        current_state, path = frontier.popleft()
        nodes_expanded += 1

        for next_state, action in get_successors(current_state):
            if next_state not in explored:
                if next_state == goal_state:
                    print(f"Goal reached! Total states expanded: {nodes_expanded}")
                    return path + [action]

                explored.add(next_state)
                frontier.append((next_state, path + [action]))

    return None  


def print_board(state):
    """Utility function to render the 3x3 board."""
    for i in range(0, 9, 3):
        row = [str(x) if x != 0 else "_" for x in state[i:i+3]]
        print("  " + " ".join(row))
    print()


start_state = (
  0, 1, 3,
  4, 2, 5,
  7, 8, 6
)

print("Initial State:")
print_board(start_state)

plan = solve_bfs(start_state)

if plan:
  print(f"Optimal Plan ({len(plan)} actions): {' -> '.join(plan)}\n")
  
  curr = start_state
  for step_num, act in enumerate(plan, 1):
      for next_st, a in get_successors(curr):
          if a == act:
              curr = next_st
              break
      print(f"Step {step_num}: Slide {act}")
      print_board(curr)
else:
  print("No valid plan found.")
