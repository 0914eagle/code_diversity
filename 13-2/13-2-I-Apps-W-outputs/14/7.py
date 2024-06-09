
def solve(n, A, dice):
    # Initialize a dictionary to store the number of values for which each dice couldn't show
    cant_show = {i: 0 for i in range(1, max(dice) + 1)}

    # Iterate over the dice and calculate the number of values for which each dice couldn't show
    for i in range(n):
        for j in range(1, dice[i] + 1):
            if A - j >= 0:
                cant_show[j] += 1

    # Return the number of values for which each dice couldn't show
    return [cant_show[i] for i in range(1, max(dice) + 1)]

