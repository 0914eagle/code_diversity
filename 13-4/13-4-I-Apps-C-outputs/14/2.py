
def solve(N, E, roads):
    # Initialize the solution matrix
    solution = [[0] * E for _ in range(N)]

    # Loop through each road
    for i in range(E):
        # Get the cities connected by the road
        city1, city2 = roads[i]

        # If the cities have not been assigned a chain yet, assign the first chain to the road
        if solution[city1][0] == 0 and solution[city2][0] == 0:
            solution[city1][0] = 1
            solution[city2][0] = 2

        # If one of the cities has already been assigned a chain, assign the other chain to the road
        elif solution[city1][0] == 0:
            solution[city1][0] = 2
            solution[city2][0] = 1
        elif solution[city2][0] == 0:
            solution[city1][0] = 1
            solution[city2][0] = 2

        # If both cities have been assigned a chain, check if the solution is valid
        else:
            # If the solution is not valid, return "0"
            if solution[city1][0] == solution[city2][0]:
                return "0"

    # If the solution is valid, return the solution matrix
    return solution

