
def solve():
    # Read input
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # Initialize variables
    satisfaction_points = 0
    current_dish = 1

    # Loop through each dish
    for i in range(N):
        # Add satisfaction points for current dish
        satisfaction_points += B[i]

        # Check if next dish is available
        if i < N - 1:
            # Add additional satisfaction points if next dish is same as current dish
            if A[i] == A[i + 1]:
                satisfaction_points += C[i]

        # Update current dish
        current_dish = A[i]

    # Return sum of satisfaction points
    return satisfaction_points

