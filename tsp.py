
import random

distance = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0]
]

cities = len(distance)

def tour_cost(route):
    cost = 0

    for i in range(cities - 1):
        cost += distance[route[i]][route[i + 1]]

    cost += distance[route[-1]][route[0]]

    return cost

def get_neighbors(route):
    neighbors = []

    for i in range(1, cities):
        for j in range(i + 1, cities):
            new_route = route[:]
            new_route[i], new_route[j] = new_route[j], new_route[i]
            neighbors.append(new_route)

    return neighbors

def local_beam_search(k=3):
    beam = []

    for _ in range(k):
        route = list(range(cities))
        random.shuffle(route[1:])
        beam.append(route)

    best_route = min(beam, key=tour_cost)
    best_cost = tour_cost(best_route)

    while True:
        candidates = []

        for route in beam:
            candidates.extend(get_neighbors(route))

        unique_candidates = []
        for route in candidates:
            if route not in unique_candidates:
                unique_candidates.append(route)

        if not unique_candidates:
            break

        unique_candidates.sort(key=tour_cost)
        new_beam = unique_candidates[:k]

        new_cost = tour_cost(new_beam[0])

        if new_cost >= best_cost:
            break

        beam = new_beam
        best_route = beam[0]
        best_cost = new_cost

    return best_route, best_cost

route, cost = local_beam_search()

print("Best Route:", route)
print("Minimum Distance:", cost)
