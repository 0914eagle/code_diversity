
def solve(n, a, m, queries):
    # Initialize an array to store the water levels
    water_levels = [0] * (n + 1)

    # Loop through each query
    for query in queries:
        # If the query is of type 1, add the water to the corresponding vessel
        if query[0] == 1:
            water_levels[query[1]] += query[2]
        # If the query is of type 2, print the water level in the corresponding vessel
        else:
            print(water_levels[query[1]])

    # Return the final water levels
    return water_levels

