
import sys

def solve(N, X, A):
    # Initialize the count of integers not exceeding X to 0
    count = 0
    
    # Iterate through the given integers A_i
    for i in range(N):
        # Check if A_i is not greater than X
        if A[i] <= X:
            # Increment the count
            count += 1
    
    # Return the count modulo 998244353
    return count % 998244353

if __name__ == '__main__':
    # Read the input from stdin
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Solve the problem
    print(solve(N, X, A))

