
def solve(a, b):
    # Initialize a dictionary to store the number of ways for each dice roll
    ways = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    # Iterate over each dice roll from 1 to 6
    for roll in range(1, 7):
        # Calculate the absolute difference between the roll and both numbers
        diff_a = abs(roll - a)
        diff_b = abs(roll - b)

        # If the first player wins, increment the number of ways for that dice roll
        if diff_a < diff_b:
            ways[roll] += 1
        # If the game ends in a draw, increment the number of ways for that dice roll
        elif diff_a == diff_b:
            ways[roll] += 1

    # Return the number of ways for each outcome
    return ways[1], ways[2], ways[3], ways[4], ways[5], ways[6]

