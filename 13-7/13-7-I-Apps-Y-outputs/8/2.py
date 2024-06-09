
def solve(N, K, A):
    # Sort the array of integers
    A.sort()
    # Initialize the minimum number of balls to rewrite
    min_balls = 0
    # Loop through the array of integers
    for i in range(N):
        # Check if the current integer is not equal to the previous integer
        if i == 0 or A[i] != A[i-1]:
            # Check if the current integer is not equal to the next integer
            if i == N-1 or A[i] != A[i+1]:
                # Increment the minimum number of balls to rewrite
                min_balls += 1
                # Check if the minimum number of balls to rewrite is greater than K
                if min_balls > K:
                    # Return -1 to indicate that it is not possible to rewrite the integers on at most K balls
                    return -1
    # Return the minimum number of balls to rewrite
    return min_balls

