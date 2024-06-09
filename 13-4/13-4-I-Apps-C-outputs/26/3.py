
import math

def solve(N, K):
    # Calculate the number of possible sequences
    num_sequences = math.factorial(N)
    
    # Calculate the number of palindromic sequences
    num_palindromes = math.floor(N / 2)
    
    # Calculate the number of sequences after one iteration
    num_sequences_after_iteration = num_palindromes * (K - 1) ** (N - 1)
    
    # Calculate the number of sequences after K iterations
    num_sequences_after_K_iterations = num_sequences_after_iteration ** K
    
    # Calculate the number of sequences after N iterations
    num_sequences_after_N_iterations = num_sequences_after_K_iterations ** (N // K)
    
    # Calculate the final answer
    final_answer = num_sequences_after_N_iterations % (10 ** 9 + 7)
    
    return final_answer

