
def equal_prices(n, k, prices):
    # Sort the prices in non-decreasing order
    prices.sort()
    # Initialize the minimum difference between prices as k
    min_diff = k
    # Initialize the equal price as the first price
    equal_price = prices[0]
    # Iterate through the prices
    for i in range(1, n):
        # Calculate the difference between the current price and the equal price
        diff = abs(prices[i] - equal_price)
        # If the difference is less than the minimum difference, update the minimum difference and the equal price
        if diff < min_diff:
            min_diff = diff
            equal_price = prices[i]
    # Return the equal price
    return equal_price

def main():
    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        prices = list(map(int, input().split()))
        print(equal_prices(n, k, prices))

if __name__ == '__main__':
    main()

