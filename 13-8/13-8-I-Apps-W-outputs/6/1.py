
import math

def solve(D, q, queries):
    # Initialize a dictionary to store the number of shortest paths between each pair of vertices
    num_paths = {}

    # Iterate over each query
    for v, u in queries:
        # If the query has already been processed, return the result
        if (v, u) in num_paths:
            continue

        # Initialize the number of shortest paths to 0
        num_paths[(v, u)] = 0

        # Iterate over each divisor of D
        for d in range(1, int(math.sqrt(D)) + 1):
            # If d is a divisor of both v and u, and d is prime
            if v % d == 0 and u % d == 0 and is_prime(d):
                # Increment the number of shortest paths by the number of divisors of v that are not divisors of u
                num_paths[(v, u)] += count_divisors(v, d) - count_divisors(u, d)

        # Return the result modulo 998244353
        num_paths[(v, u)] %= 998244353

    # Return the number of shortest paths for each query
    return [num_paths[(v, u)] for v, u in queries]

def count_divisors(n, d):
    # Count the number of divisors of n that are not divisors of d
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % d != 0 and n // i % d != 0:
                count += 1
    if int(math.sqrt(n)) ** 2 == n:
        count -= 1
    return count

def is_prime(n):
    # Check if n is prime
    if n == 1 or n == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

queries = [(4, 4), (12, 1), (3, 4)]
print(solve(12, 3, queries))

