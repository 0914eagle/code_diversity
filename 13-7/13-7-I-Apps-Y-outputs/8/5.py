
def solve(N, K, A):
    # Sort the array of integers
    A.sort()
    # Initialize the minimum number of balls to rewrite
    min_balls = 0
    # Initialize the current number of different integers
    current_diff = len(set(A))
    # Loop through the array of integers
    for i in range(N):
        # If the current number of different integers is less than or equal to K, we don't need to rewrite any more balls
        if current_diff <= K:
            break
        # If the current integer is different from the previous integer, we need to rewrite the current ball
        if i == 0 or A[i] != A[i-1]:
            min_balls += 1
        # Update the current number of different integers
        current_diff -= 1
    return min_balls

