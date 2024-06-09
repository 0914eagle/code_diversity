
def solve(n, a, b, k, health):
    # Calculate the maximum number of points that can be gained by fighting the monsters
    max_points = 0
    for i in range(n):
        # If the monster is dead, skip it
        if health[i] <= 0:
            continue
        # If the monster is not dead, calculate the number of points that can be gained by fighting it
        points = (health[i] - 1) // a
        # If the monster is not dead after being hit, calculate the number of points that can be gained by skipping its turn
        if health[i] > a:
            points += 1
        # Update the maximum number of points
        max_points = max(max_points, points)
    return max_points

