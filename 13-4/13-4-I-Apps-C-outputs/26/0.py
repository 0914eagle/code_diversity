
import math

def solve(N, K):
    # Calculate the number of possible sequences
    num_sequences = math.factorial(N)
    
    # Calculate the number of palindromic sequences
    num_palindromic_sequences = math.floor(num_sequences / 2)
    
    # Calculate the number of sequences after one iteration
    num_sequences_after_iteration = num_palindromic_sequences * (K - 1)
    
    # Calculate the number of sequences after N iterations
    num_sequences_after_N_iterations = num_sequences_after_iteration ** N
    
    # Return the result modulo 10^9+7
    return num_sequences_after_N_iterations % 1000000007

