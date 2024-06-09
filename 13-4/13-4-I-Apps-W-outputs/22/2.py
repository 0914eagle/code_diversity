
def solve(H, N, A, B):
    # Initialize the minimum total Magic Points to infinity
    min_points = float('inf')
    # Loop through each spell
    for i in range(N):
        # Calculate the total Magic Points needed to cast the spell
        total_points = A[i] * H // B[i]
        # If the total Magic Points needed is less than the minimum, update the minimum
        if total_points < min_points:
            min_points = total_points
    # Return the minimum total Magic Points needed to win
    return min_points

