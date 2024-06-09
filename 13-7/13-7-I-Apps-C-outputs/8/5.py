
def solve(N, Q, queries):
    # Initialize the number of stones in each box to 0
    num_stones = [0] * (N + 1)
    # Initialize the probability of each box to 1/N
    probabilities = [1/N] * (N + 1)

    for query in queries:
        # If the query is of type 1, update the number of stones in the box and the probability of the box
        if query[0] == 1:
            u, v = query[1], query[2]
            num_stones[u] += 1
            num_stones[v] += 1
            probabilities[u] = (probabilities[u] * (N - 1) + 1) / N
            probabilities[v] = (probabilities[v] * (N - 1) + 1) / N
        # If the query is of type 2, calculate the expected value of the sum of the squares of the number of stones in each box
        elif query[0] == 2:
            expected_value = 0
            for i in range(1, N + 1):
                expected_value += num_stones[i] ** 2 * probabilities[i]
            print(int(expected_value % 1000000007))

if __name__ == '__main__':
    N, Q = map(int, input().split())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    solve(N, Q, queries)

