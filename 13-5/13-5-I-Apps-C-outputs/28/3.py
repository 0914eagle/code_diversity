
import math

def count_ways(N, M, K):
    # Calculate the binomial coefficient (N choose K)
    binom = math.factorial(N) // math.factorial(K) // math.factorial(N - K)
    # Calculate the number of ways to choose M copies of each object
    ways = binom * math.factorial(M) // math.factorial(M - 1)
    # Return the result modulo 10^6 + 7
    return ways % (10**6 + 7)

