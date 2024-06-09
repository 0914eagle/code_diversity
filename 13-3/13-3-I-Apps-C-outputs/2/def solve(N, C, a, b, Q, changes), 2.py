
def solve(N, C, a, b, Q, changes):
    # Initialize the number of different purchases
    num_purchases = 0
    
    # Loop through each change in requirements
    for change in changes:
        # Get the client and their new requirements
        client, new_a, new_b = change
        
        # Check if the client wants colored paintings
        if new_a > 0:
            # Add the number of colored paintings to the total
            num_purchases += new_a
        
        # Check if the client wants black and white paintings
        if new_b > 0:
            # Add the number of black and white paintings to the total
            num_purchases += new_b
    
    # Return the number of different purchases modulo 10007
    return num_purchases % 10007

