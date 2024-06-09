
def solve(N, K):
    # Calculate the number of possible sequences
    num_sequences = (K ** N) * (K - 1)
    
    # Since the sequence is a palindrome, we need to divide by 2 since we can have the same sequence but with the first and last elements swapped
    num_sequences //= 2
    
    # Return the result modulo 10^9 + 7
    return num_sequences % (10**9 + 7)

