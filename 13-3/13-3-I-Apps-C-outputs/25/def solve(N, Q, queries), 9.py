
def solve(N, Q, queries):
    # Initialize the number of stones in each box to 0
    stones = [0] * (N + 1)
    
    # Loop through each query
    for query in queries:
        # If the query is of type 1, add a stone to the box between u and v
        if query[0] == 1:
            stones[query[1]] += 1
            stones[query[2]] += 1
        # If the query is of type 2, calculate the expected value of A
        else:
            # Calculate the sum of the squares of the number of stones in each box
            sum_squares = sum([stone**2 for stone in stones])
            # Return the result modulo 10^9 + 7
            return sum_squares % (10**9 + 7)
