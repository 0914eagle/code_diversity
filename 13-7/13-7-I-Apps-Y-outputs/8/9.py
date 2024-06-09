
def solve(N, K, A):
    # Sort the array of integers
    A.sort()
    # Initialize the minimum number of balls to rewrite as 0
    min_balls = 0
    # Iterate through the array of integers
    for i in range(N):
        # Check if the current integer is equal to the previous integer
        if i > 0 and A[i] == A[i-1]:
            # If they are equal, continue to the next iteration
            continue
        # Check if the current integer is equal to the next integer
        if i < N-1 and A[i] == A[i+1]:
            # If they are equal, continue to the next iteration
            continue
        # Check if the current integer is not equal to the previous or next integer
        if i > 0 and i < N-1 and A[i] != A[i-1] and A[i] != A[i+1]:
            # If they are not equal, increment the minimum number of balls to rewrite
            min_balls += 1
    # Return the minimum number of balls to rewrite
    return min_balls

