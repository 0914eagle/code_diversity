
import math

def solve(D, q, queries):
    # Initialize a dictionary to store the number of shortest paths between each pair of vertices
    num_paths = {}

    # Initialize a set to store the prime divisors of D
    prime_divisors = set()

    # Iterate through the divisors of D, starting from 2
    for d in range(2, int(math.sqrt(D)) + 1):
        # If d is a prime divisor of D, add it to the set of prime divisors
        if D % d == 0:
            prime_divisors.add(d)

    # Iterate through the queries
    for v, u in queries:
        # Initialize the number of shortest paths between v and u to 0
        num_paths[(v, u)] = 0

        # Iterate through the divisors of v and u
        for d in range(1, int(math.sqrt(v)) + 1):
            # If d is a divisor of both v and u, and d is not a prime divisor of D, add it to the number of shortest paths between v and u
            if v % d == 0 and u % d == 0 and d not in prime_divisors:
                num_paths[(v, u)] += 1

    # Return the number of shortest paths between each pair of vertices
    return [num_paths[(v, u)] % 998244353 for v, u in queries]

