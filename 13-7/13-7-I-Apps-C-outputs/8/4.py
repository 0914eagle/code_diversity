
import math

def solve(N, Q, queries):
    # Initialize the number of stones in each box to 0
    num_stones = [0] * (N + 1)
    # Initialize the probability of each box to 1
    probabilities = [1] * (N + 1)

    for query in queries:
        # If the query is of type 1, put a stone inside one of the boxes between u and v
        if query[0] == 1:
            u, v = query[1], query[2]
            for i in range(u, v + 1):
                num_stones[i] += 1
                probabilities[i] = probabilities[i] * (1 - 1 / N)
        # If the query is of type 2, calculate the expected value of the sum of the squares of the number of stones in each box
        else:
            expected_value = 0
            for i in range(1, N + 1):
                expected_value += num_stones[i] ** 2 * probabilities[i]
            print(int(expected_value % 1000000007))

if __name__ == '__main__':
    N, Q = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    solve(N, Q, queries)

