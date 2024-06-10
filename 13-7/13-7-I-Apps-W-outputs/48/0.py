
def get_maximum_bourles(n, m, r, s, b):
    # Initialize the maximum number of bourles to hold
    max_bourles = r
    
    # Iterate over the opportunities to buy shares
    for i in range(n):
        # Check if buying shares at the current price is profitable
        if s[i] <= max_bourles:
            # Update the maximum number of bourles to hold
            max_bourles = max_bourles - s[i]
    
    # Iterate over the opportunities to sell shares
    for i in range(m):
        # Check if selling shares at the current price is profitable
        if b[i] >= max_bourles:
            # Update the maximum number of bourles to hold
            max_bourles = max_bourles + b[i]
    
    # Return the maximum number of bourles to hold
    return max_bourles

def main():
    # Read the input
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Get the maximum number of bourles to hold
    max_bourles = get_maximum_bourles(n, m, r, s, b)
    
    # Print the result
    print(max_bourles)

if __name__ == '__main__':
    main()

