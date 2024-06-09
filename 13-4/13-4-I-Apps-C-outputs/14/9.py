
def solve_problem(N, E, roads):
    # Initialize the solution matrix
    solution = [[0] * E for _ in range(N)]

    # Loop through each road
    for i in range(E):
        # Get the cities connected by the road
        city1, city2 = roads[i]

        # If the cities are not already assigned, assign them to the first chain
        if solution[city1][i] == 0:
            solution[city1][i] = 1
        if solution[city2][i] == 0:
            solution[city2][i] = 2

        # If the cities are already assigned, check if the assignment is valid
        else:
            # If the cities are assigned to the same chain, the solution is not valid
            if solution[city1][i] == solution[city2][i]:
                return "0"

            # If the cities are assigned to different chains, the solution is valid
            else:
                solution[city1][i] = solution[city2][i]

    # If the solution is valid, return it
    return solution

