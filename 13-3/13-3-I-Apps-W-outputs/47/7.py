
def solve(N, towns):
    # Sort the towns by their x-coordinates
    sorted_towns = sorted(towns, key=lambda town: town[0])

    # Initialize the minimum cost to 0
    min_cost = 0

    # Loop through the towns and build roads between them
    for i in range(N-1):
        # Get the current and next town
        current_town = sorted_towns[i]
        next_town = sorted_towns[i+1]

        # Calculate the cost of the road between the current and next town
        cost = abs(current_town[0] - next_town[0])

        # Add the cost to the minimum cost
        min_cost += cost

    return min_cost

