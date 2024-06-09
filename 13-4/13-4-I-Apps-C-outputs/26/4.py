
import math

def solve(N, K):
    # Calculate the number of possible sequences
    num_sequences = math.factorial(N)
    
    # Calculate the number of palindromic sequences
    num_palindromes = math.floor(N / 2)
    
    # Calculate the number of sequences that can be obtained after the procedure
    num_sequences_after_procedure = num_sequences - num_palindromes
    
    # Return the result modulo 10^9+7
    return num_sequences_after_procedure % 1000000007

