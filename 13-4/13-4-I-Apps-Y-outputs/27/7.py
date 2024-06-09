
def solve(n, a, b, k, health):
    # Calculate the maximum points that can be gained by fighting the monsters
    max_points = 0
    for i in range(n):
        if health[i] <= 0:
            continue
        max_points += 1
        health[i] -= a
        if health[i] <= 0:
            health[i] = 0
    
    # Use the secret technique to skip turns
    for i in range(k):
        for j in range(n):
            if health[j] <= 0:
                continue
            health[j] -= b
            if health[j] <= 0:
                health[j] = 0
                break
    
    # Calculate the final points
    final_points = 0
    for i in range(n):
        if health[i] > 0:
            final_points += 1
    
    return max_points + final_points

