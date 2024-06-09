
import math

def f1(N, Q):
    # Initialize the number of stones in each box to 0
    num_stones = [0] * (N + 1)
    # Initialize the probability of each box to 1/N
    probabilities = [1/N] * (N + 1)
    
    # Loop through each query
    for _ in range(Q):
        # Read the query
        query = input().split()
        # If the query is to put a stone in a box
        if query[0] == "1":
            # Get the indices of the boxes
            u, v = map(int, query[1:])
            # Update the number of stones in each box
            num_stones[u] += 1
            num_stones[v] += 1
            # Update the probability of each box
            for i in range(u, v + 1):
                probabilities[i] = (probabilities[i] * (num_stones[i] - 1) + 1/N) / num_stones[i]
        # If the query is to calculate the expected value
        elif query[0] == "2":
            # Calculate the expected value
            expected_value = 0
            for i in range(1, N + 1):
                expected_value += probabilities[i] * num_stones[i] ** 2
            # Print the result
            print(int(expected_value % (10**9 + 7)))

def f2(...):
    # TODO: Implement function 2
    pass

if __name__ == '__main__':
    N, Q = map(int, input().split())
    f1(N, Q)

