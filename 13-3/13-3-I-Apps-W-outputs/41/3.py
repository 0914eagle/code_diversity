
def get_max_total_damage(n, a, b, health, damage):
    # Initialize the maximum total damage
    max_total_damage = 0
    
    # Loop through each creature
    for i in range(n):
        # Get the current creature's health and damage
        current_health = health[i]
        current_damage = damage[i]
        
        # Check if the first spell can be used
        if a > 0:
            # Double the current creature's health
            current_health *= 2
            # Decrement the number of first spell uses
            a -= 1
        
        # Check if the second spell can be used
        if b > 0:
            # Assign the current creature's health to its damage
            current_damage = current_health
            # Decrement the number of second spell uses
            b -= 1
        
        # Add the current creature's damage to the maximum total damage
        max_total_damage += current_damage
    
    # Return the maximum total damage
    return max_total_damage

