
import math

def solve(n, k):
    mod = 1000000007
    # Calculate the number of possible sequences
    num_sequences = math.factorial(k) * math.factorial(n - 1)
    # Calculate the number of palindromic sequences
    num_palindromes = math.factorial(n)
    # Calculate the number of sequences that can be obtained after the procedure
    num_obtained = num_sequences - num_palindromes + 1
    return num_obtained % mod

