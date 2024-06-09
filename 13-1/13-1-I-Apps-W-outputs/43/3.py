
def brutality(n, k, a, s):
    # Initialize variables
    dmg = 0
    curr_button = ''
    count = 0
    
    # Iterate through the hits
    for i in range(n):
        # If the current button is the same as the previous button
        if s[i] == curr_button:
            # Increment the count
            count += 1
        else:
            # Reset the count
            count = 1
        
        # If the count is less than or equal to the maximum allowed consecutive presses
        if count <= k:
            # Add the damage to the total damage
            dmg += a[i]
        
        # Update the current button
        curr_button = s[i]
    
    # Return the total damage
    return dmg

