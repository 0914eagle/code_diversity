
def solve(N, C, a, b, Q, changes):
    # Initialize the number of different purchases
    num_purchases = 0
    
    # Loop through each change in requirements
    for change in changes:
        # Get the client and their new requirements
        client, new_a, new_b = change
        
        # If the client wants at least one colored painting
        if new_a > 0:
            # Increment the number of different purchases
            num_purchases += 1
        
        # If the client wants at least one black and white painting
        if new_b > 0:
            # Increment the number of different purchases
            num_purchases += 1
    
    # Return the number of different purchases modulo 10007
    return num_purchases % 10007

