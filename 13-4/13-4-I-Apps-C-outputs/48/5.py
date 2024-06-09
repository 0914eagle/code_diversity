
import sys

def solve(N, X, A):
    # Initialize the count of different integers not exceeding X to 0
    count = 0
    
    # Iterate through the given integers A_1, A_2, ..., A_N
    for i in range(N):
        # Check if the current integer A_i is not greater than X
        if A[i] <= X:
            # Increment the count of different integers not exceeding X
            count += 1
    
    # Return the count of different integers not exceeding X
    return count

if __name__ == '__main__':
    # Read the input data from stdin
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Solve the problem
    count = solve(N, X, A)
    
    # Print the count modulo 998244353
    print(count % 998244353)

