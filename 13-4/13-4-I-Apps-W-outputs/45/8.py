
def get_max_sweets(n, s, prices):
    # Sort the prices in non-decreasing order
    prices.sort(key=lambda x: x[1])

    # Initialize the maximum number of sweets to 0
    max_sweets = 0

    # Iterate through the prices and calculate the maximum number of sweets
    for price in prices:
        dollars, cents = price
        if s >= dollars:
            max_sweets += cents
            s -= dollars
        else:
            max_sweets += s * 100
            break

    # Return the maximum number of sweets
    return max_sweets

