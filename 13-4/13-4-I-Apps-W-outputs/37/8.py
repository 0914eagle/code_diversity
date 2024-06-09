
def solve(x):
    # Initialize the minimum number of operations to be infinity
    min_operations = float('inf')
    # Iterate over all possible values of the side facing upward
    for i in range(1, 7):
        # Calculate the total points that can be obtained by rotating the die
        total_points = 0
        for j in range(1, 7):
            if (i + j) % 6 == 0:
                total_points += j
        # If the total points are greater than or equal to x, return the minimum number of operations needed
        if total_points >= x:
            return min_operations
        # Otherwise, update the minimum number of operations if needed
        min_operations = min(min_operations, total_points // x + 1)
    # If no side faces upward can obtain at least x points, return -1
    return -1

