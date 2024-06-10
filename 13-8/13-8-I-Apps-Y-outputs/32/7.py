
def equalize_prices(n, k, a):
    # Sort the prices in non-decreasing order
    a.sort()
    # Initialize the minimum difference between prices
    min_diff = a[1] - a[0]
    # Loop through the prices and find the minimum difference
    for i in range(1, n-1):
        diff = a[i+1] - a[i]
        if diff < min_diff:
            min_diff = diff
    # Return the maximum price that satisfies the condition
    return a[n-1] + k - min_diff

def main():
    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(equalize_prices(n, k, a))

if __name__ == '__main__':
    main()

