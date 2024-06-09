
def solve(N, Q, queries):
    # Initialize the number of stones in each box to 0
    num_stones = [0] * (N + 1)
    # Initialize the expected value to 0
    expected_value = 0

    for query in queries:
        # If the query is of type 1, Linux puts a stone inside one of the boxes between u and v
        if query[0] == 1:
            u, v = query[1], query[2]
            # Increment the number of stones in the box between u and v
            num_stones[u] += 1
            num_stones[v] += 1
        # If the query is of type 2, Linux asks Bash to compute E(A)
        else:
            # Calculate the expected value of A
            expected_value = sum(num_stone ** 2 for num_stone in num_stones)
            # Print the expected value modulo 10^9 + 7
            print(expected_value % (10 ** 9 + 7))

solve(2, 4, [[1, 1, 2], [2], [1, 1, 2], [2]])

