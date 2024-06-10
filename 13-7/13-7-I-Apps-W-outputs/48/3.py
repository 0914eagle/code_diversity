
def get_maximum_bourles(n, m, r, s, b):
    # Initialize the maximum number of bourles to 0
    max_bourles = 0
    # Loop through each opportunity to buy shares
    for i in range(n):
        # Check if the current price is less than or equal to the number of bourles available
        if s[i] <= r:
            # Calculate the number of shares that can be bought with the current price
            shares = r // s[i]
            # Update the number of bourles available
            r -= shares * s[i]
            # Add the current price to the maximum number of bourles
            max_bourles += shares * s[i]
    # Loop through each opportunity to sell shares
    for i in range(m):
        # Check if the current price is less than or equal to the number of bourles available
        if b[i] <= max_bourles:
            # Calculate the number of shares that can be sold with the current price
            shares = max_bourles // b[i]
            # Update the number of bourles available
            max_bourles -= shares * b[i]
    # Return the maximum number of bourles
    return max_bourles

def main():
    # Read the input data
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Call the function to get the maximum number of bourles
    max_bourles = get_maximum_bourles(n, m, r, s, b)
    # Print the maximum number of bourles
    print(max_bourles)

if __name__ == '__main__':
    main()

