
def get_min_price_to_obtain_all_vitamins(n, prices, vitamins):
    # Initialize a dictionary to store the count of vitamins for each juice
    vitamin_count = {}
    for i in range(n):
        vitamin_count[i] = 0
        for vitamin in vitamins[i]:
            vitamin_count[i] += 1

    # Sort the juices by the number of vitamins they contain, in descending order
    sorted_juices = sorted(range(n), key=lambda i: vitamin_count[i], reverse=True)

    # Initialize the minimum total price to obtain all vitamins as the price of the first juice
    min_price = prices[sorted_juices[0]]

    # Iterate through the sorted juices and add the price of each juice if it contains a vitamin that is not yet obtained
    for i in sorted_juices:
        if vitamin_count[i] > 0:
            min_price += prices[i]
            vitamin_count[i] -= 1

    # If all three vitamins are obtained, return the minimum total price, otherwise return -1
    if vitamin_count == {0, 0, 0}:
        return min_price
    else:
        return -1

