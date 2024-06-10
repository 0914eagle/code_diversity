
def get_max_bourles(n, m, r, s, b):
    # Initialize variables
    max_bourles = r
    shares = 0
    
    # Iterate over the opportunities to buy shares
    for i in range(n):
        # If we have enough money to buy the shares, buy them
        if r >= s[i]:
            shares += r // s[i]
            r %= s[i]
    
    # Iterate over the opportunities to sell shares
    for i in range(m):
        # If we have shares to sell, sell them
        if shares > 0:
            max_bourles = max(max_bourles, shares * b[i])
            shares -= min(shares, b[i])
    
    return max_bourles

def main():
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_max_bourles(n, m, r, s, b))

if __name__ == '__main__':
    main()

