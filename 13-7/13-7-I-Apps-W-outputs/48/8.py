
def get_max_bourles(n, m, r, s, b):
    # Initialize the maximum number of bourles to be 0
    max_bourles = 0
    
    # Loop through each opportunity to buy shares
    for i in range(n):
        # Calculate the total cost of buying i shares at the current price
        total_cost = s[i] * i
        
        # If the total cost is less than or equal to the current number of bourles, buy i shares
        if total_cost <= r:
            r -= total_cost
    
    # Loop through each opportunity to sell shares
    for i in range(m):
        # Sell all shares at the current price
        r += b[i] * i
    
    # Return the maximum number of bourles
    return r

def main():
    # Read the input
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Call the get_max_bourles function and print the result
    print(get_max_bourles(n, m, r, s, b))

if __name__ == '__main__':
    main()

