
def solve(N, E, roads):
    # Initialize the solution matrix
    solution = [[0] * E for _ in range(N)]

    # Loop through each road
    for i in range(E):
        # Get the cities connected by the road
        city1, city2 = roads[i]

        # If the road is not yet assigned to a chain
        if solution[city1][i] == 0 and solution[city2][i] == 0:
            # Assign the road to the first chain
            solution[city1][i] = 1
            solution[city2][i] = 1

    # Check if the solution is valid
    for i in range(N):
        # If a city has no roads assigned to it, return "0"
        if sum(solution[i]) == 0:
            return "0"

    # If the solution is valid, return the assignment of roads to chains
    return ["1" if solution[i][j] == 1 else "2" for i in range(N) for j in range(E)]

