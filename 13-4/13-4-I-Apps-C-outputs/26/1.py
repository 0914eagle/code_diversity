
def solve(N, K):
    # Calculate the number of possible sequences
    num_sequences = (K ** N) * (K + 1) // 2
    
    # Calculate the number of palindromic sequences
    num_palindromes = 0
    for i in range(1, K + 1):
        num_palindromes += 1
    
    # Calculate the number of sequences after the procedure
    num_sequences_after_procedure = num_palindromes * (N // 2)
    
    # Return the result modulo 10^9 + 7
    return num_sequences_after_procedure % 1000000007

