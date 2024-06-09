
import sys

def f1(N, S):
    # Calculate the number of palindromic strings of length 2N
    num_palindromes = (2 * N) * (2 * N + 1) // 2
    
    # Calculate the number of palindromic strings of length 2N that contain S as a subsequence
    num_subsequence_palindromes = 0
    for i in range(N):
        # Check if the ith character of S is also in the ith character of the reverse of S
        if S[i] == S[N-i-1]:
            num_subsequence_palindromes += 1
    
    return num_palindromes - num_subsequence_palindromes

def f2(N, S):
    # Calculate the number of palindromic strings of length 2N that contain S as a subsequence
    num_subsequence_palindromes = 0
    for i in range(N):
        # Check if the ith character of S is also in the ith character of the reverse of S
        if S[i] == S[N-i-1]:
            num_subsequence_palindromes += 1
    
    return num_subsequence_palindromes

if __name__ == '__main__':
    N = int(input())
    S = input()
    print(f1(N, S))
    print(f2(N, S))

