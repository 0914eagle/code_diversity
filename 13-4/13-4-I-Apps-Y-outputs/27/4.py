
def solve(n, a, b, k, hp):
    # Calculate the maximum number of points that can be gained by attacking the monsters
    max_points = 0
    for i in range(n):
        # If the monster is dead, skip it
        if hp[i] <= 0:
            continue
        # If the monster is not dead, calculate the number of points that can be gained by attacking it
        points = (hp[i] - 1) // a
        # If the monster is dead after being attacked, add the number of points to the total
        if (hp[i] - 1) % a == 0:
            max_points += points
        # If the monster is not dead, calculate the number of points that can be gained by attacking it and then skipping the next monster
        if i + 1 < n and k > 0:
            points = (hp[i] - b) // a
            if (hp[i] - b) % a == 0:
                max_points += points
        # If the monster is not dead and the secret technique can be used, calculate the number of points that can be gained by attacking it and then skipping the next monster
        if i + 2 < n and k > 1:
            points = (hp[i] - 2 * b) // a
            if (hp[i] - 2 * b) % a == 0:
                max_points += points
    return max_points

