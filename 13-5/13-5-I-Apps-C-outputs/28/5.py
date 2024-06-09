
import math

def solve(N, M, K):
    # Calculate the binomial coefficient (N choose K)
    choose = math.factorial(N) // math.factorial(K) // math.factorial(N - K)

    # Calculate the number of ways to take K objects from M copies of each object
    ways = choose * math.factorial(M - 1)

    # Return the result modulo 10^6 + 7
    return ways % (10**6 + 7)

