
import math

def count_ways(N, M, K):
    # Calculate the binomial coefficient (N choose K)
    num = math.factorial(N) // math.factorial(K) // math.factorial(N - K)
    
    # Calculate the number of ways to choose M copies of each object
    den = math.factorial(M) ** K
    
    # Return the result modulo 10^6 + 7
    return num // den % 1000007

