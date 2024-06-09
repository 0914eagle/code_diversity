
def solve(n, a, b, k, h):
    # Calculate the maximum points that can be gained by fighting the monsters
    max_points = 0
    for i in range(n):
        max_points += max(0, h[i] - a)
    
    # If the number of monsters is less than or equal to the number of times the secret technique can be used, return the maximum points
    if n <= k:
        return max_points
    
    # Initialize the minimum points that need to be gained to skip the next monster
    min_points = 10**9 + 1
    
    # Iterate over the monsters
    for i in range(n):
        # If the current monster has more health points than the minimum points needed to skip the next monster, update the minimum points
        if h[i] > min_points:
            min_points = h[i]
    
    # Return the maximum of the maximum points that can be gained by fighting the monsters and the minimum points needed to skip the next monster
    return max(max_points, min_points)

