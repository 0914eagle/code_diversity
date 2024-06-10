
def equalize_prices(n, k, prices):
    # Sort the prices in non-decreasing order
    prices.sort()
    # Initialize the maximum equal price as the smallest price
    equal_price = prices[0]
    # Iterate through the prices and calculate the maximum equal price
    for i in range(1, n):
        # Calculate the difference between the current price and the equal price
        diff = prices[i] - equal_price
        # If the difference is greater than k, return -1
        if diff > k:
            return -1
        # Update the equal price to be the current price
        equal_price = prices[i]
    # Return the maximum equal price
    return equal_price

def main():
    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        prices = list(map(int, input().split()))
        print(equalize_prices(n, k, prices))

if __name__ == '__main__':
    main()

