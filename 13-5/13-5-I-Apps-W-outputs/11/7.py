
def solve(a, b):
    # Initialize a dictionary to store the number of ways for each dice roll
    d = {}

    # Iterate over all possible dice rolls
    for i in range(1, 7):
        # Calculate the absolute difference between the dice roll and the numbers written by the players
        abs_diff_a = abs(i - a)
        abs_diff_b = abs(i - b)

        # If the absolute difference is the same, it's a draw
        if abs_diff_a == abs_diff_b:
            d[i] = 0
        # Otherwise, the player with the smaller absolute difference wins
        elif abs_diff_a < abs_diff_b:
            d[i] = 1
        else:
            d[i] = 2

    # Return the number of ways for each outcome
    return (d[1], d[2], d[3], d[4], d[5], d[6])

