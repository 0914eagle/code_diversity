
def get_minimum_cost(n, prices, vitamins):
    # Initialize a dictionary to store the count of vitamins for each juice
    vitamin_count = {}
    for i in range(n):
        vitamin_count[i] = 0
        for vitamin in vitamins[i]:
            vitamin_count[i] += 1

    # Sort the juices by the number of vitamins they contain, in descending order
    sorted_juices = sorted(range(n), key=lambda i: vitamin_count[i], reverse=True)

    # Initialize the minimum cost to obtain all three vitamins
    minimum_cost = 0

    # Iterate through the sorted juices and add the cost of the juice if it contains a vitamin that has not been obtained yet
    for i in sorted_juices:
        if vitamin_count[i] > 0:
            minimum_cost += prices[i]
            vitamin_count[i] -= 1

    # If all three vitamins have been obtained, return the minimum cost, otherwise return -1
    if minimum_cost == 3:
        return minimum_cost
    else:
        return -1

