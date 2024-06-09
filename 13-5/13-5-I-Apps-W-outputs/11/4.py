
def solve(a, b):
    # Initialize a dictionary to store the number of ways for each dice roll
    ways = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    # Iterate over each dice roll from 1 to 6
    for roll in range(1, 7):
        # Calculate the difference between the dice roll and the numbers written by the players
        diff_a = abs(roll - a)
        diff_b = abs(roll - b)

        # If the difference between the dice roll and the first player's number is less than or equal to the difference between the dice roll and the second player's number, the first player wins
        if diff_a <= diff_b:
            ways[roll] += 1
        # If the differences are equal, it's a draw
        elif diff_a == diff_b:
            ways[roll] += 0.5
        # Otherwise, the second player wins
        else:
            ways[roll] += 0

    # Return the number of ways for each outcome
    return ways[1], ways[2], ways[3], ways[4], ways[5], ways[6]

