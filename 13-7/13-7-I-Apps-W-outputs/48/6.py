
def get_maximum_bourles(n, m, r, s, b):
    # Initialize variables
    max_bourles = 0
    shares = 0
    for i in range(n):
        # Buy shares
        shares += r // s[i]
        r %= s[i]
    for i in range(m):
        # Sell shares
        max_bourles += min(shares, b[i]) * b[i]
        shares -= min(shares, b[i])
    return max_bourles

def main():
    # Read input
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Calculate maximum bourles
    max_bourles = get_maximum_bourles(n, m, r, s, b)
    # Print result
    print(max_bourles)

if __name__ == '__main__':
    main()

