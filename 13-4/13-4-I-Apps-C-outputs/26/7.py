
import math

def solve(N, K):
    # Calculate the number of possible sequences
    num_sequences = math.factorial(N)
    
    # Calculate the number of palindromes
    num_palindromes = 0
    for i in range(1, K+1):
        num_palindromes += 1
    
    # Calculate the number of sequences that are not palindromes
    num_non_palindromes = num_sequences - num_palindromes
    
    # Calculate the number of sequences after the procedure
    num_sequences_after_procedure = num_non_palindromes
    
    # Return the result modulo 10^9+7
    return num_sequences_after_procedure % 1000000007

