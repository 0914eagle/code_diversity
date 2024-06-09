
def solve(N, C, a, b, Q, changes):
    # Initialize the number of different purchases
    num_purchases = 0
    
    # Loop through each change in requirements
    for change in changes:
        # Get the person and their new requirements
        person, new_a, new_b = change
        
        # If the person wants more colored paintings than before
        if new_a > a[person-1]:
            # Add the difference to the number of different purchases
            num_purchases += new_a - a[person-1]
        
        # If the person wants more black and white paintings than before
        if new_b > b[person-1]:
            # Add the difference to the number of different purchases
            num_purchases += new_b - b[person-1]
        
        # Update the person's requirements
        a[person-1] = new_a
        b[person-1] = new_b
    
    # Return the number of different purchases modulo 10007
    return num_purchases % 10007

