
import sys

def solve(N, X, A):
    # Initialize the count of integers not exceeding X to 0
    count = 0
    
    # Iterate over the given integers
    for i in range(N):
        # Convert the integer to binary
        binary = bin(A[i])[2:]
        
        # Initialize a variable to store the current integer
        current = 0
        
        # Iterate over the binary representation of the integer
        for j in range(len(binary)):
            # If the current bit is 1, add the corresponding power of 2 to the current integer
            if binary[j] == "1":
                current += 2**j
            
            # If the current integer is not greater than X, increment the count
            if current <= X:
                count += 1
    
    # Return the count modulo 998244353
    return count % 998244353

if __name__ == "__main__":
    # Read the input from stdin
    N, X = list(map(int, input().split()))
    A = list(map(int, input().split()))
    
    # Solve the problem
    print(solve(N, X, A))

