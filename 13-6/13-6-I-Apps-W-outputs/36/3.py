
def get_min_price(n, prices, vitamins):
    # Initialize a dictionary to store the count of vitamins for each juice
    vitamin_count = {}
    for i in range(n):
        vitamin_count[i] = 0
        for vitamin in vitamins[i]:
            vitamin_count[i] += 1

    # Sort the juices by the count of vitamins in descending order
    sorted_juices = sorted(vitamin_count.items(), key=lambda x: x[1], reverse=True)

    # Initialize the minimum total price and the count of vitamins obtained
    min_price = 0
    vitamins_obtained = 0

    # Iterate through the sorted juices and add the price of the juice if it contains a vitamin that Petya hasn't obtained yet
    for juice, count in sorted_juices:
        if vitamins_obtained < 3:
            min_price += prices[juice]
            vitamins_obtained += 1

    # If Petya has obtained all three vitamins, return the minimum total price, otherwise return -1
    if vitamins_obtained == 3:
        return min_price
    else:
        return -1

