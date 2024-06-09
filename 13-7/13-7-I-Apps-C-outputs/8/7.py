
def solve(N, Q, queries):
    # Initialize the number of stones in each box to 0
    num_stones = [0] * (N + 1)
    # Initialize the probability of each box having a stone to 0
    prob_stone = [0] * (N + 1)
    
    # Loop through each query
    for query in queries:
        # If the query is to put a stone inside a box
        if query[0] == 1:
            # Get the indices of the two boxes
            u, v = query[1], query[2]
            # Loop through each box between u and v, inclusive
            for i in range(u, v + 1):
                # Add 1 to the number of stones in the box
                num_stones[i] += 1
                # Add the probability of the box having a stone
                prob_stone[i] += 1 / (v - u + 1)
        # If the query is to calculate the expected value of A
        elif query[0] == 2:
            # Initialize the sum of the squares of the number of stones to 0
            sum_squares = 0
            # Loop through each box
            for i in range(1, N + 1):
                # Add the product of the number of stones and the probability of the box having a stone to the sum of the squares
                sum_squares += num_stones[i] * prob_stone[i]
            # Return the result modulo 10^9 + 7
            return sum_squares % (10**9 + 7)

# Test the function with the sample input
N, Q = 2, 4
queries = [[1, 1, 2], [2], [1, 1, 2], [2]]
print(solve(N, Q, queries))

# Test the function with a larger input
N, Q = 1000, 100000
queries = [[1, 1, 1000], [2]] * Q
print(solve(N, Q, queries))

