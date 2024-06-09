
def solve(n, a, b, k, h):
    # Calculate the maximum points that can be gained by fighting the monsters
    max_points = 0
    for i in range(n):
        max_points += max(0, h[i] - a)
    
    # If the number of monsters is less than or equal to the number of times the secret technique can be used, return the maximum points
    if n <= k:
        return max_points
    
    # Initialize the variables to keep track of the maximum points that can be gained by using the secret technique
    max_points_with_technique = 0
    current_points = 0
    current_monster = 0
    
    # Loop through the monsters
    for i in range(n):
        # If the current monster has more health points than the opponent's attack power, the opponent will die and the current monster will be skipped
        if h[i] > b:
            current_points += 1
            current_monster += 1
            continue
        
        # If the current monster has less health points than the opponent's attack power, the current monster will die and the opponent will gain a point
        current_points -= 1
        
        # If the current monster is the last monster, return the maximum points that can be gained by using the secret technique
        if i == n - 1:
            return max_points_with_technique
        
        # If the current monster is not the last monster and the number of times the secret technique can be used is not exhausted, use the secret technique to skip the current monster and move on to the next one
        if current_monster < k:
            current_monster += 1
            current_points += 1
            max_points_with_technique = max(max_points_with_technique, current_points)
    
    # Return the maximum points that can be gained by using the secret technique
    return max_points_with_technique

