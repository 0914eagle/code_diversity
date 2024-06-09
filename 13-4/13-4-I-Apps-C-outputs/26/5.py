
import math

def solve(N, K):
    mod = 1000000007
    # Initialize the result with the number of palindromes with length N and elements between 1 and K
    result = count_palindromes(N, K)
    
    # If N is odd, then the first element can be moved to the end an odd number of times,
    # so we need to add the number of palindromes with length N-1 and elements between 1 and K
    if N % 2 == 1:
        result = (result + count_palindromes(N-1, K)) % mod
    
    return result

def count_palindromes(N, K):
    # Base case: if N is 1, then there is only one palindrome with length 1 and elements between 1 and K
    if N == 1:
        return 1
    
    # Initialize the result with the number of palindromes with length N-2 and elements between 1 and K
    result = count_palindromes(N-2, K)
    
    # If N is even, then the first and last elements can be the same, so we need to add the number of palindromes with length N-2 and elements between 1 and K-1
    if N % 2 == 0:
        result = (result + count_palindromes(N-2, K-1)) % 1000000007
    
    return result

