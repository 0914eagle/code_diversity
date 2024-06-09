
def solve(N, Q, queries):
    # Initialize the number of stones in each box to 0
    stones = [0] * (N + 1)
    
    # Loop through each query
    for query in queries:
        # If the query is to put a stone in a box
        if query[0] == 1:
            # Get the indices of the two boxes
            u, v = query[1], query[2]
            
            # Put a stone in one of the boxes between u and v, inclusive
            stones[u + (v - u) // 2] += 1
        
        # If the query is to calculate the expected value of A
        elif query[0] == 2:
            # Calculate the expected value of A
            expected_A = 0
            for i in range(1, N + 1):
                expected_A += stones[i] ** 2
            
            # Return the expected value of A modulo 10^9 + 7
            return expected_A % (10**9 + 7)
    
    # If all queries have been processed, return -1
    return -1

