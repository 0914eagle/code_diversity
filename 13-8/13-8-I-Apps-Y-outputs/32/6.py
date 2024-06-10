
def get_equal_prices(n, k, a):
    # Sort the prices in ascending order
    a.sort()
    # Initialize the minimum difference between prices
    min_diff = k + 1
    # Initialize the equal price
    equal_price = -1
    # Iterate over the prices
    for i in range(n):
        # Calculate the difference between the current price and the equal price
        diff = abs(a[i] - equal_price)
        # If the difference is less than or equal to the minimum difference, update the equal price and the minimum difference
        if diff <= min_diff:
            equal_price = a[i]
            min_diff = diff
    # If the minimum difference is less than or equal to the given value of k, return the equal price
    # Otherwise, return -1
    return equal_price if min_diff <= k else -1

def main():
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_equal_prices(n, k, a))

if __name__ == '__main__':
    main()

