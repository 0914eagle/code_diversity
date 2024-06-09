
def solve(N, K, healths):
    # Sort the healths in descending order
    healths.sort(reverse=True)
    # Initialize the number of attacks needed
    attacks_needed = 0
    # Loop through the healths and calculate the number of attacks needed for each monster
    for i in range(N):
        # If the monster's health is greater than or equal to the number of attacks needed,
        # then the monster can be killed with an attack
        if healths[i] >= attacks_needed:
            # Increment the number of attacks needed
            attacks_needed += 1
        # If the monster's health is less than the number of attacks needed,
        # then the monster can be killed with a special move
        else:
            # Increment the number of attacks needed
            attacks_needed += 1
            # If the number of special moves used is less than or equal to K,
            # then use a special move on the current monster
            if K > 0:
                # Decrement the number of special moves used
                K -= 1
                # Increment the number of attacks needed
                attacks_needed += 1
    # Return the minimum number of attacks needed to win
    return attacks_needed

