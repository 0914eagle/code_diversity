
def solve(a, b):
    # Initialize a dictionary to store the number of ways for each dice roll
    ways = {i: 0 for i in range(1, 7)}

    # Loop through each dice roll and calculate the difference between the written numbers and the dice roll
    for i in range(1, 7):
        diff_a = abs(a - i)
        diff_b = abs(b - i)

        # If the difference between the written numbers is the same, it's a draw
        if diff_a == diff_b:
            ways[i] += 1
        # If the first player's written number is closer to the dice roll, they win
        elif diff_a < diff_b:
            ways[i] += 1
        # If the second player's written number is closer to the dice roll, they win
        else:
            ways[i] += 0

    # Return the number of ways for each outcome
    return (ways[1], ways[2], ways[3], ways[4], ways[5], ways[6])

