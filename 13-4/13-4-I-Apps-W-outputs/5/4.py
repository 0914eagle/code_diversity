
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

        # If the query has already been processed, return the stored value
        if (v, u) in num_paths:
            continue

        # Initialize the number of shortest paths to 0
        num_paths[(v, u)] = 0

        # Iterate over each divisor of D
        for d in range(1, int(math.sqrt(D)) + 1):
            # If d is a divisor of both v and u, and d is prime, increment the number of shortest paths
            if v % d == 0 and u % d == 0 and is_prime(d):
                num_paths[(v, u)] += 1

        # Modulo the number of shortest paths by 998244353 to ensure it fits in the required range
        num_paths[(v, u)] %= 998244353

    # Return the number of shortest paths for each query
    return [num_paths[(v, u)] for v, u in queries]

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
result = solve(D, q, queries)
print(*result, sep='\n')

