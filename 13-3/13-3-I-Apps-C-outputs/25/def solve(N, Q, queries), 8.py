
def solve(N, Q, queries):
    # Initialize the number of stones in each box to 0
    num_stones = [0] * (N + 1)
    # Initialize the expected value of the sum of squares to 0
    expected_sum = 0
    # Loop through each query
    for query in queries:
        # If the query is of type 1, put a stone inside one of the boxes between u and v
        if query[0] == 1:
            u, v = query[1], query[2]
            # Add 1 to the number of stones in the box between u and v
            for i in range(u, v + 1):
                num_stones[i] += 1
        # If the query is of type 2, calculate the expected value of the sum of squares
        else:
            # Calculate the expected value of the sum of squares using the number of stones in each box
            for i in range(1, N + 1):
                expected_sum += num_stones[i] ** 2
            # Return the expected value modulo 10^9 + 7
            return expected_sum % (10**9 + 7)

