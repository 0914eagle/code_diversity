
def equalize_prices(n, k, prices):
    # Sort the prices in non-decreasing order
    prices.sort()
    # Initialize the minimum difference between prices
    min_diff = float('inf')
    # Initialize the equal price
    equal_price = 0
    # Iterate over the prices
    for i in range(n):
        # Calculate the difference between the current price and the equal price
        diff = abs(prices[i] - equal_price)
        # If the difference is less than or equal to k, set the equal price to the current price
        if diff <= k:
            equal_price = prices[i]
        # If the difference is greater than k, update the minimum difference
        else:
            min_diff = min(min_diff, diff - k)
    # If the minimum difference is greater than k, it is impossible to equalize the prices
    if min_diff > k:
        return -1
    # Return the equal price
    return equal_price

def main():
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        prices = list(map(int, input().split()))
        print(equalize_prices(n, k, prices))

if __name__ == '__main__':
    main()

