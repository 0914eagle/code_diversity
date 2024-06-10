
def equalize_prices(n, k, a):
    # Sort the prices in ascending order
    a.sort()
    # Initialize the minimum difference between prices
    min_diff = k + 1
    # Initialize the equal price
    equal_price = -1
    # Iterate over the prices
    for i in range(n - 1):
        # Calculate the difference between the current price and the next price
        diff = a[i + 1] - a[i]
        # If the difference is less than or equal to the minimum difference, update the minimum difference and the equal price
        if diff <= min_diff:
            min_diff = diff
            equal_price = (a[i] + a[i + 1]) // 2
    # If the minimum difference is less than or equal to the given value of k, return the equal price
    if min_diff <= k:
        return equal_price
    # Otherwise, return -1
    return -1

def main():
    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(equalize_prices(n, k, a))

if __name__ == '__main__':
    main()

