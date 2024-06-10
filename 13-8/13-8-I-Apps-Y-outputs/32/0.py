
def equalize_prices(a, k):
    # Sort the prices in non-decreasing order
    a.sort()
    # Initialize the minimum difference between prices
    min_diff = k + 1
    # Initialize the equal price
    equal_price = 0
    # Iterate over the prices
    for i in range(len(a)):
        # Calculate the difference between the current price and the equal price
        diff = abs(a[i] - equal_price)
        # If the difference is less than the minimum difference, update the minimum difference and the equal price
        if diff < min_diff:
            min_diff = diff
            equal_price = a[i]
    # Return the equal price
    return equal_price

def main():
    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(equalize_prices(a, k))

if __name__ == '__main__':
    main()

