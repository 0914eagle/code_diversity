
def solve(N, A, B, healths):
    # Sort the healths in descending order
    healths.sort(reverse=True)
    
    # Initialize the number of explosions needed to vanish all monsters
    explosions_needed = 0
    
    # Loop through the healths and cause explosions until all monsters are vanished
    while sum(healths) > 0:
        # Find the index of the monster with the highest health
        highest_index = healths.index(max(healths))
        
        # Cause an explosion centered at the monster with the highest health
        healths[highest_index] -= A
        
        # Decrease the healths of the other monsters by B
        for i in range(len(healths)):
            if i != highest_index:
                healths[i] -= B
        
        # Remove any monsters with health <= 0
        healths = [x for x in healths if x > 0]
        
        # Increment the number of explosions needed
        explosions_needed += 1
    
    return explosions_needed

