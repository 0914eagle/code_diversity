
def get_max_damage(n, a, b, health, damage):
    # Initialize the maximum total damage as 0
    max_damage = 0
    
    # Loop through each creature
    for i in range(n):
        # Use the first spell on the creature
        health[i] *= 2
        damage[i] += health[i]
        max_damage += damage[i]
        
        # Use the second spell on the creature
        damage[i] = health[i]
        max_damage += damage[i]
    
    return max_damage

