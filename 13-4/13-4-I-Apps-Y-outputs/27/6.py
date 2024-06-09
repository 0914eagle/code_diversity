
def solve(n, a, b, k, hp):
    # Calculate the maximum number of points that can be gained by fighting the monsters
    max_points = 0
    for i in range(n):
        # If the monster is dead, skip it
        if hp[i] <= 0:
            continue
        # If the monster is not dead, calculate the number of points that can be gained by fighting it
        points = (hp[i] - 1) // a
        # If the monster is dead after being hit, add the points to the total
        if (hp[i] - 1) % a == 0:
            max_points += points
        # If the monster is not dead, calculate the number of points that can be gained by skipping it
        if k > 0:
            max_points += 1
            k -= 1
    return max_points

