
def solve(H, n, d):
    # Calculate the total damage dealt by the monster each round
    total_damage = sum(d)
    
    # If the total damage is greater than or equal to the monster's initial hp,
    # the monster will die within the first round
    if total_damage >= H:
        return 1
    
    # Initialize a variable to keep track of the current hp of the monster
    current_hp = H
    
    # Iterate through each minute of the battle
    for i in range(1, n+1):
        # Calculate the damage dealt by the monster in the current minute
        damage = d[i-1]
        
        # Update the current hp of the monster
        current_hp += damage
        
        # If the current hp of the monster is less than or equal to 0,
        # the monster has died, so return the current minute
        if current_hp <= 0:
            return i
    
    # If the battle continues infinitely, return -1
    return -1

