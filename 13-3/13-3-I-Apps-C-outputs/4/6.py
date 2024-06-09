
import sys

def solve(N, X, A):
    # Initialize the count of integers not exceeding X to 0
    count = 0
    
    # Loop through each integer in A
    for i in range(N):
        # If the integer is not greater than X, increment the count
        if A[i] <= X:
            count += 1
    
    # Return the count modulo 998244353
    return count % 998244353

if __name__ == '__main__':
    # Read the input from stdin
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Solve the problem
    print(solve(N, X, A))

