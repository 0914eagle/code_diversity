
def get_min_price(n, prices, vitamins):
    # Initialize a dictionary to store the count of vitamins for each juice
    vitamin_count = {}
    for i in range(n):
        vitamin_count[i] = 0
        for vitamin in vitamins[i]:
            vitamin_count[i] += 1

    # Sort the juices by their price in non-decreasing order
    sorted_juices = sorted(range(n), key=lambda i: prices[i])

    # Initialize the minimum total price to obtain all three vitamins as -1
    min_price = -1

    # Iterate through the sorted juices and check if they contain all three vitamins
    for i in sorted_juices:
        if vitamin_count[i] == 3:
            min_price = prices[i]
            break

    return min_price

