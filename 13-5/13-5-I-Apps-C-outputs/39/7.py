
def f1(N, S):
    # Calculate the number of palindromic strings of length 2N
    num_palindromes = (2*N) * (2*N-1) // 2
    
    # Calculate the number of palindromic strings of length 2N that contain S
    num_containing_S = 0
    for i in range(len(S)):
        # Check if the substring S[i:i+N] is a palindrome
        if S[i:i+N] == S[i:i+N][::-1]:
            num_containing_S += 1
    
    return num_containing_S

def f2(N, S):
    # Calculate the number of palindromic strings of length 2N that contain S
    num_containing_S = f1(N, S)
    
    # Calculate the number of palindromic strings of length 2N that do not contain S
    num_not_containing_S = num_palindromes - num_containing_S
    
    # Return the result modulo 10^9+7
    return num_not_containing_S % (10**9+7)

if __name__ == '__main__':
    N = int(input())
    S = input()
    print(f2(N, S))

