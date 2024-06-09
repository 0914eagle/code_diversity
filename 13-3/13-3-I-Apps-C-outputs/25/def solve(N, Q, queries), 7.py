
def solve(N, Q, queries):
    # Initialize the number of stones in each box to 0
    stones = [0] * (N + 1)
    
    # Loop through each query
    for query in queries:
        # If the query is of type 1, put a stone inside a box between u and v
        if query[0] == 1:
            u, v = query[1], query[2]
            stones[u] += 1
            stones[v] += 1
        # If the query is of type 2, calculate the expected value of A
        else:
            # Calculate the sum of the squares of the number of stones in each box
            A = sum([stones[i]**2 for i in range(1, N+1)])
            # Return the result modulo 10^9 + 7
            return A % (10**9 + 7)

