
def solve(x):
    # Initialize the minimum number of operations to be infinity
    min_ops = float('inf')
    # Iterate over all possible values of the die
    for i in range(1, 7):
        # Calculate the sum of the two numbers on opposite sides
        sum_opposite = i + (7 - i)
        # Check if the sum is greater than or equal to x
        if sum_opposite >= x:
            # If the sum is greater than or equal to x, the minimum number of operations is 1
            min_ops = 1
            break
        # If the sum is less than x, calculate the minimum number of operations required to reach x
        else:
            # Calculate the number of operations required to reach x by rotating the die towards the left
            left_ops = (x - sum_opposite) // 2
            # Calculate the number of operations required to reach x by rotating the die towards the right
            right_ops = (x - sum_opposite) // 2 + 1
            # Update the minimum number of operations if the current number of operations is less than the minimum
            min_ops = min(min_ops, left_ops, right_ops)
    # Return the minimum number of operations
    return min_ops

