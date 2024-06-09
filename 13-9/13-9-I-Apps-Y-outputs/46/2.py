
def solve(N, M):
    # Initialize a count variable to 0
    count = 0
    
    # Iterate over the even numbers from 0 to 2N
    for i in range(0, 2*N+1, 2):
        # Iterate over the odd numbers from 1 to 2M
        for j in range(1, 2*M+1, 2):
            # Check if the sum of i and j is even
            if (i + j) % 2 == 0:
                # Increment the count
                count += 1
    
    # Return the count
    return count

