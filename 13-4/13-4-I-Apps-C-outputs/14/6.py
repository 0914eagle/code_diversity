
import sys

def get_input():
    n, e = map(int, input().split())
    roads = []
    for i in range(e):
        a, b = map(int, input().split())
        roads.append((a, b))
    return n, e, roads

def is_connected(roads, city, chain):
    for road in roads:
        if road[0] == city and road[1] != chain:
            return True
    return False

def solve(n, e, roads):
    # Initialize the solution matrix
    solution = [[0 for _ in range(n)] for _ in range(n)]

    # Iterate through each road
    for i in range(e):
        # Get the two cities connected by this road
        city1, city2 = roads[i]

        # If both cities have a restaurant from the first chain, skip this road
        if solution[city1][1] == 1 and solution[city2][1] == 1:
            continue

        # If both cities have a restaurant from the second chain, skip this road
        if solution[city1][2] == 1 and solution[city2][2] == 1:
            continue

        # If one of the cities has a restaurant from the first chain and the other has a restaurant from the second chain, skip this road
        if (solution[city1][1] == 1 and solution[city2][2] == 1) or (solution[city1][2] == 1 and solution[city2][1] == 1):
            continue

        # If neither city has a restaurant from either chain, assign the road to the first chain
        if solution[city1][1] == 0 and solution[city1][2] == 0 and solution[city2][1] == 0 and solution[city2][2] == 0:
            solution[city1][1] = 1
            solution[city2][1] = 1
            continue

        # If one city has a restaurant from the first chain and the other city is not connected to any other chain, assign the road to the first chain
        if solution[city1][1] == 1 and solution[city2][1] == 0 and not is_connected(roads, city2, 1):
            solution[city2][1] = 1
            continue

        # If one city has a restaurant from the second chain and the other city is not connected to any other chain, assign the road to the second chain
        if solution[city1][2] == 1 and solution[city2][2] == 0 and not is_connected(roads, city2, 2):
            solution[city2][2] = 1
            continue

        # If both cities are not connected to any other chain, assign the road to the first chain
        if not is_connected(roads, city1, 1) and not is_connected(roads, city1, 2) and not is_connected(roads, city2, 1) and not is_connected(roads, city2, 2):
            solution[city1][1] = 1
            solution[city2][1] = 1
            continue

        # If none of the above conditions are met, the solution is not unique
        return "0"

    # If all roads have been assigned, return the solution
    return [str(solution[i][1]) for i in range(n)]

n, e, roads = get_input()
print("\n".join(solve(n, e, roads)))

