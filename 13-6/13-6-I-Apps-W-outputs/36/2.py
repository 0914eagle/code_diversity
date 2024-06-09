
def get_min_price(n, prices, vitamins):
    # Initialize a dictionary to store the count of vitamins for each juice
    vitamin_count = {}
    for i in range(n):
        vitamin_count[i] = 0
        for vitamin in vitamins[i]:
            vitamin_count[i] += 1

    # Sort the juices by the count of vitamins in descending order
    sorted_juices = sorted(vitamin_count.items(), key=lambda x: x[1], reverse=True)

    # Initialize the minimum total price to 0
    min_price = 0

    # Iterate through the sorted juices and add the price of the juice if it contains at least one vitamin
    for juice, count in sorted_juices:
        if count > 0:
            min_price += prices[juice]

    return min_price

