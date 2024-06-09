
def solve(n, A, dice):
    # Initialize the number of values for which each dice couldn't show
    b = [0] * n

    # Iterate over each dice
    for i in range(n):
        # Get the maximum value that the current dice can show
        max_value = dice[i]

        # Iterate over each value from 1 to the maximum value of the current dice
        for value in range(1, max_value + 1):
            # Check if the current value is possible with the given sum and dice
            if is_possible(A, dice, value, i):
                # If it is possible, then the current dice couldn't show this value
                b[i] += 1

    return b

def is_possible(A, dice, value, i):
    # Initialize the sum of the values shown by the dice
    sum = 0

    # Iterate over each dice
    for j in range(len(dice)):
        # If it is not the current dice, then add the maximum value it can show to the sum
        if i != j:
            sum += dice[j]

    # Return True if the sum plus the current value is equal to the given sum, False otherwise
    return sum + value == A

