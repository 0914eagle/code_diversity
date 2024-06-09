
def solve(N, M):
    # Initialize a counter for the number of even sums
    count = 0
    
    # Iterate over all possible sums
    for i in range(1, N+M+1):
        # Check if the sum is even
        if i % 2 == 0:
            # Count the number of ways to choose two balls with this sum
            count += 1
    
    # Return the number of ways to choose two balls with an even sum
    return count

