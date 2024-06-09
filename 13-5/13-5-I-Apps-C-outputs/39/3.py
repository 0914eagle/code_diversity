
def f1(N, S):
    # calculate the number of palindromic strings of length 2N
    num_palindromes = (2 * N) * (2 * N + 1) // 2
    
    # calculate the number of palindromic strings of length 2N that contain S as a subsequence
    num_containing_S = 0
    for i in range(N):
        # check if the ith character of S is also in the ith character of the palindrome
        if S[i] in S:
            num_containing_S += 1
    
    return num_palindromes - num_containing_S

def f2(N, S):
    # calculate the number of palindromic strings of length 2N
    num_palindromes = (2 * N) * (2 * N + 1) // 2
    
    # calculate the number of palindromic strings of length 2N that contain S as a subsequence
    num_containing_S = 0
    for i in range(N):
        # check if the ith character of S is also in the ith character of the palindrome
        if S[i] in S:
            num_containing_S += 1
    
    return num_containing_S

if __name__ == '__main__':
    N = int(input())
    S = input()
    print(f1(N, S))
    print(f2(N, S))

