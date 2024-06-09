
def solve(N, Q, queries):
    # Initialize the number of stones in each box to 0
    stones = [0] * (N + 1)
    
    # Loop through each query
    for query in queries:
        # If the query is of type 1, put a stone in the box between u and v
        if query[0] == 1:
            stones[query[1]] += 1
            stones[query[2]] += 1
        # If the query is of type 2, calculate the expected value of A
        else:
            # Calculate the probability that two stones are in different squares
            prob = (stones[1] * (stones[N] - stones[1]) + stones[N] * (stones[1] - stones[N])) / (stones[1] * stones[N])
            
            # Calculate the expected value of A
            expected_A = prob * (stones[1]**2 + stones[N]**2) + (1 - prob) * (stones[1]**2 + 2 * stones[N]**2)
            
            # Print the expected value of A modulo 10^9 + 7
            print(expected_A % (10**9 + 7))

