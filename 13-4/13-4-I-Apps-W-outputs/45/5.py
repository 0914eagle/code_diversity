
def get_max_sweets(n, s, prices):
    # Sort the prices in non-decreasing order
    prices.sort(key=lambda x: x[1])

    # Initialize the maximum number of sweets to 0
    max_sweets = 0

    # Iterate through the prices and calculate the maximum number of sweets
    for i in range(n):
        # Calculate the cost of the current type of sugar
        cost = prices[i][0] * 100 + prices[i][1]

        # If the cost is less than or equal to the amount of money Caisa has, buy the sugar and calculate the number of sweets as change
        if cost <= s:
            max_sweets += s - cost

            # Subtract the cost of the current type of sugar from the amount of money Caisa has
            s -= cost

    # Return the maximum number of sweets
    return max_sweets

