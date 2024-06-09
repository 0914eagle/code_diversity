
import sys

def solve(N, X, A):
    # Initialize the count of integers not exceeding X to 0
    count = 0
    
    # Iterate over the given integers
    for i in range(N):
        # Convert the current integer to binary
        curr_bin = bin(A[i])[2:]
        
        # Initialize a variable to store the result of the current integer
        result = 0
        
        # Iterate over the binary representation of the current integer
        for j in range(len(curr_bin)):
            # If the current bit is 1, add the corresponding power of 2 to the result
            if curr_bin[j] == '1':
                result += 2**j
        
        # Add the result to the count
        count += result
    
    # Return the count modulo 998244353
    return count % 998244353

if __name__ == '__main__':
    # Read the input from stdin
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Solve the problem
    print(solve(N, X, A))

