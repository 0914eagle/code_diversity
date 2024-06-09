
import math

def permutations_of_order_k(n, k):
    # Calculate the number of permutations of n elements of order k
    # Modulo 2^31 - 1 to avoid overflow
    num_permutations = math.factorial(n) // math.factorial(n - k)
    return num_permutations % (2**31 - 1)

