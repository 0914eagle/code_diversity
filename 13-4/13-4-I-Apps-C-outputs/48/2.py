
import sys

def solve(N, X, A):
    # Initialize the count of different integers not exceeding X to 0
    count = 0
    
    # Loop through each integer A_i
    for i in range(N):
        # Check if A_i is less than or equal to X
        if A[i] <= X:
            # Increment the count
            count += 1
    
    # Return the count modulo 998244353
    return count % 998244353

if __name__ == '__main__':
    # Read the input from stdin
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Call the solve function and print the result
    print(solve(N, X, A))

