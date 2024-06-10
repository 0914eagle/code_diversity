
def get_max_bourles(n, m, r, s, b):
    # Initialize the maximum number of bourles to 0
    max_bourles = 0
    
    # Loop through the opportunities to buy shares
    for i in range(n):
        # Calculate the number of shares that can be bought with the current opportunity
        num_shares = r // s[i]
        
        # Calculate the amount of bourles that can be spent on the current opportunity
        cost = num_shares * s[i]
        
        # If the cost is less than or equal to the current amount of bourles, update the maximum number of bourles
        if cost <= r:
            max_bourles = max(max_bourles, r - cost)
    
    # Loop through the opportunities to sell shares
    for i in range(m):
        # Calculate the number of shares that can be sold with the current opportunity
        num_shares = r // b[i]
        
        # Calculate the amount of bourles that can be earned from the current opportunity
        earnings = num_shares * b[i]
        
        # If the earnings are greater than or equal to the current amount of bourles, update the maximum number of bourles
        if earnings >= r:
            max_bourles = max(max_bourles, earnings - r)
    
    return max_bourles

def main():
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_max_bourles(n, m, r, s, b))

if __name__ == '__main__':
    main()

