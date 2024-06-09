
def solve(a, b):
    # Initialize a dictionary to store the number of ways for each dice roll
    ways = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    # Iterate over each dice roll from 1 to 6
    for i in range(1, 7):
        # Calculate the absolute difference between the dice roll and both numbers
        diff_a = abs(i - a)
        diff_b = abs(i - b)

        # If the first player's number is closer to the dice roll, add 1 to their way count
        if diff_a < diff_b:
            ways[i] += 1
        # If the second player's number is closer to the dice roll, add 1 to their way count
        elif diff_b < diff_a:
            ways[i] -= 1
        # If both numbers are equal, it's a draw, so add 1 to the draw count
        else:
            ways[i] += 1

    # Return the number of ways for each outcome
    return (ways[1], ways[2], ways[3], ways[4], ways[5], ways[6])

