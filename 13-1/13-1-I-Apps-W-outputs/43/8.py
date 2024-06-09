
def brutality(n, k, a, s):
    # Initialize variables
    dmg = 0
    curr_button = ''
    consecutive_presses = 0

    # Iterate through the hits
    for i in range(n):
        # Get the current hit and button
        curr_hit = a[i]
        curr_button = s[i]

        # Check if the button is the same as the previous button
        if curr_button == curr_button:
            # Increment the consecutive presses counter
            consecutive_presses += 1
        else:
            # Reset the consecutive presses counter
            consecutive_presses = 1

        # Check if the consecutive presses counter is greater than k
        if consecutive_presses > k:
            # Skip the current hit
            continue
        else:
            # Add the current hit to the total damage
            dmg += curr_hit

    # Return the total damage
    return dmg

