
def solve(N, A, B, C):
    # Initialize variables
    satisfaction_points = 0
    current_dish = 0

    # Loop through each dish
    for i in range(N):
        # Add satisfaction points from current dish
        satisfaction_points += B[current_dish]

        # If not the last dish, add satisfaction points from next dish
        if i != N - 1:
            next_dish = A[i + 1]
            if next_dish == current_dish + 1:
                satisfaction_points += C[current_dish]

        # Update current dish
        current_dish = A[i]

    return satisfaction_points

