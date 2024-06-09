
def get_max_sweets(n, s, sugar_prices):
    # Sort the sugar prices in non-decreasing order of price
    sugar_prices.sort(key=lambda x: x[0])

    # Initialize the maximum number of sweets to 0
    max_sweets = 0

    # Iterate through the sugar prices and calculate the maximum number of sweets that can be bought
    for price in sugar_prices:
        dollars, cents = price
        if s >= dollars:
            max_sweets += cents
            s -= dollars
        else:
            break

    # If there are still dollars left, it's not possible to buy any sugar
    if s > 0:
        return -1

    # Return the maximum number of sweets
    return max_sweets

