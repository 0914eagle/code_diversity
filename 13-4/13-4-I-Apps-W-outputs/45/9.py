
def get_max_sweets(n, s, prices):
    # Sort the prices in descending order
    prices.sort(key=lambda x: x[0], reverse=True)

    # Initialize the maximum number of sweets to 0
    max_sweets = 0

    # Iterate through the prices and calculate the maximum number of sweets that can be bought
    for price in prices:
        dollars, cents = price
        if s >= dollars:
            max_sweets += cents
            s -= dollars

    # If there is still money left, return -1
    if s > 0:
        return -1

    # Return the maximum number of sweets
    return max_sweets

