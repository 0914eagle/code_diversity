
import math

def f1(N, Q, queries):
    # Initialize the number of stones in each box to 0
    num_stones = [0] * (N + 1)
    
    # Loop through each query
    for query in queries:
        # If the query is of type 1, put a stone in the box between u and v
        if query[0] == 1:
            u, v = query[1], query[2]
            num_stones[u] += 1
            num_stones[v] += 1
        # If the query is of type 2, calculate the expected value of A
        else:
            expected_value = 0
            for i in range(1, N + 1):
                expected_value += num_stones[i] ** 2
            return expected_value

def f2(...):
    # Implement function 2 here
    pass

if __name__ == '__main__':
    N, Q = map(int, input().split())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    result = f1(N, Q, queries)
    print(result)

