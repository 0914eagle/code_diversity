
def equalize_prices(n, k, a):
    # Sort the prices in ascending order
    a.sort()
    
    # Initialize the minimum and maximum prices
    min_price = a[0]
    max_price = a[-1]
    
    # Loop through the prices and find the minimum and maximum prices
    for i in range(1, n):
        if a[i] - a[i-1] > k:
            return -1
        min_price = min(min_price, a[i])
        max_price = max(max_price, a[i])
    
    # Return the minimum or maximum price as the answer
    return max_price

def main():
    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(equalize_prices(n, k, a))

if __name__ == '__main__':
    main()

