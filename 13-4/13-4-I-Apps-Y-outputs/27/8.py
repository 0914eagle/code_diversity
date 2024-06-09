
def solve(n, a, b, k, health):
    # Calculate the maximum points that can be gained by fighting the monsters
    max_points = 0
    for i in range(n):
        max_points += max(0, health[i] - a)
    
    # If the number of monsters is less than or equal to the number of times the secret technique can be used, return the maximum points
    if n <= k:
        return max_points
    
    # Initialize the variables to keep track of the maximum points that can be gained by using the secret technique
    max_points_with_technique = 0
    current_points = 0
    current_monster = 0
    
    # Loop through the monsters
    for i in range(n):
        # If the current monster has more health points than the opponent's attack power, the opponent will die and the current player will gain a point
        if health[i] > b:
            current_points += 1
            health[i] -= b
        # If the current monster has less health points than the opponent's attack power, the current player will die and gain no points
        else:
            current_points += 0
            health[i] -= a
        
        # If the current player has used the secret technique, skip the next monster
        if current_monster < k:
            current_monster += 1
            continue
        
        # If the current player has not used the secret technique, add the maximum points that can be gained by fighting the current monster to the total points
        max_points_with_technique += max(0, health[i] - a)
    
    # Return the maximum points that can be gained by using the secret technique optimally
    return max(max_points, max_points_with_technique)

