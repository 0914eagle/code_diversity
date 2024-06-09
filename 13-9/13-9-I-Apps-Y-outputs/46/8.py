
def solve(N, M):
    # Initialize a counter for the even sums
    count = 0
    
    # Iterate over all possible combinations of N even and M odd numbers
    for i in range(0, N+1):
        for j in range(0, M+1):
            # Check if the sum of the numbers is even
            if (i + j) % 2 == 0:
                count += 1
    
    # Return the count of even sums
    return count

