
def solve(N, E, roads):
    # Initialize the solution matrix
    solution = [[0] * E for _ in range(N)]

    # Loop through each road
    for i in range(E):
        # Get the cities connected by the road
        city1, city2 = roads[i]

        # If the cities have not been assigned yet, assign them to the first chain
        if solution[city1][0] == 0:
            solution[city1][0] = 1
        if solution[city2][0] == 0:
            solution[city2][0] = 2

        # If the cities have already been assigned, check if the current chain is the same as the previous one
        if solution[city1][0] != solution[city2][0]:
            return "0"

    # If we reach this point, the solution is valid
    return ["1" if solution[i][0] == 1 else "2" for i in range(N)]

