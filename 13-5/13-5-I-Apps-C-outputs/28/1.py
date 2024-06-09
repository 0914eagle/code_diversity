
import math

def solve(N, M, K):
    # Calculate the binomial coefficient (N choose K)
    denominator = math.factorial(N) // math.factorial(K) // math.factorial(N - K)
    # Calculate the number of ways to choose M copies of each object
    numerator = math.factorial(M) ** K
    # Calculate the final answer
    answer = numerator // denominator
    # Return the result modulo 10^6 + 7
    return answer % (10**6 + 7)

