
import math

def solve(D, q, queries):
    # Initialize a dictionary to store the number of shortest paths between each pair of vertices
    num_paths = {}

    # Iterate over each query
    for v, u in queries:
        # If the query is for the same vertex, the number of shortest paths is 1
        if v == u:
            num_paths[(v, u)] = 1
            continue

        # If the query has already been processed, return the cached result
        if (v, u) in num_paths:
            continue

        # Initialize the number of shortest paths to 0
        num_paths[(v, u)] = 0

        # Iterate over all divisors of D
        for d in range(1, int(math.sqrt(D)) + 1):
            # If d is not a divisor of v or u, continue
            if v % d != 0 or u % d != 0:
                continue

            # If d is a prime number, increment the number of shortest paths
            if is_prime(d):
                num_paths[(v, u)] += 1

        # Add the number of shortest paths for the reverse query (u, v)
        num_paths[(v, u)] += num_paths[(u, v)]

        # Print the number of shortest paths modulo 998244353
        print(num_paths[(v, u)] % 998244353)

    return num_paths

def is_prime(n):
    # Check if n is a prime number
    if n == 1 or n == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

D = int(input())
q = int(input())
queries = []
for i in range(q):
    v, u = map(int, input().split())
    queries.append((v, u))

solve(D, q, queries)

