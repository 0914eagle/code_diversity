
def solve(n, a, b, k, hp):
    # Calculate the maximum points that can be gained by fighting the monsters
    max_points = 0
    for i in range(n):
        if hp[i] <= 0:
            continue
        points = (hp[i] - 1) // a + 1
        max_points = max(max_points, points)

    # If the secret technique can be used, calculate the maximum points that can be gained by using it optimally
    if k > 0:
        # Initialize the maximum points that can be gained by using the secret technique
        max_points_with_technique = 0

        # Iterate over the possible positions of the monsters that can be skipped
        for i in range(n):
            # If the monster at position i is dead, skip it
            if hp[i] <= 0:
                continue

            # Calculate the maximum points that can be gained by fighting the monsters from position i+1 to n-1
            max_points_without_technique = 0
            for j in range(i+1, n):
                if hp[j] <= 0:
                    continue
                points = (hp[j] - 1) // b + 1
                max_points_without_technique = max(max_points_without_technique, points)

            # Calculate the maximum points that can be gained by using the secret technique on the monster at position i
            points = (hp[i] - 1) // a + 1
            max_points_with_technique = max(max_points_with_technique, points + max_points_without_technique)

        # Return the maximum points that can be gained by using the secret technique optimally
        return max_points_with_technique

    # Return the maximum points that can be gained by fighting the monsters optimally
    return max_points

