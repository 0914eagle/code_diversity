
def solve(N, Q, queries):
    # Initialize the number of stones in each box to 0
    num_stones = [0] * (N + 1)
    # Initialize the expected value of A to 0
    expected_A = 0
    
    for query in queries:
        # If the query is of type 1, add a stone to the box between u and v
        if query[0] == 1:
            u, v = query[1], query[2]
            for i in range(u, v + 1):
                num_stones[i] += 1
        # If the query is of type 2, calculate the expected value of A
        elif query[0] == 2:
            # Calculate the expected value of A for each box
            for i in range(1, N + 1):
                expected_A += num_stones[i] ** 2
            # Calculate the expected value of A modulo 10^9 + 7
            expected_A = expected_A % (10 ** 9 + 7)
    
    return expected_A

