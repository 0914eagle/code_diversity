
def solve(n, a, b, k, h):
    # Calculate the maximum number of points that can be gained by fighting the monsters
    max_points = 0
    for i in range(n):
        # If the monster is dead, skip it
        if h[i] <= 0:
            continue
        # If the monster is not dead, calculate the number of points that can be gained by fighting it
        points = (h[i] - 1) // a
        # If the monster has more than one point, add the number of points to the total
        if points > 0:
            max_points += points
        # If the monster has only one point, add it to the total and skip the next monster
        elif points == 1:
            max_points += points
            i += 1
    # Return the maximum number of points
    return max_points

