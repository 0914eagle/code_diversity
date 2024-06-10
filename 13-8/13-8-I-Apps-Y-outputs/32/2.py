
def equalize_prices(n, k, a):
    # Sort the prices in non-decreasing order
    a.sort()
    # Initialize the minimum difference between prices as k
    min_diff = k
    # Initialize the equal price as the minimum price
    equal_price = a[0]
    # Iterate over the prices
    for i in range(1, n):
        # Calculate the difference between the current price and the previous price
        diff = a[i] - a[i - 1]
        # If the difference is less than the minimum difference, update the minimum difference and equal price
        if diff < min_diff:
            min_diff = diff
            equal_price = a[i - 1]
    # Return the equal price
    return equal_price

def main():
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(equalize_prices(n, k, a))

if __name__ == '__main__':
    main()

