
def solve(n, prices, vitamins):
    # Initialize the minimum total price to obtain all three vitamins as -1
    min_price = -1
    # Iterate over the juices
    for i in range(n):
        # Check if the current juice contains all three vitamins
        if "A" in vitamins[i] and "B" in vitamins[i] and "C" in vitamins[i]:
            # If the current juice contains all three vitamins, update the minimum total price
            min_price = min(min_price, prices[i])
    # Return the minimum total price
    return min_price

