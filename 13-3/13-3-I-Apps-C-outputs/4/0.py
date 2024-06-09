
import sys

def solve(N, X, A):
    # Initialize the count of integers not exceeding X to 0
    count = 0
    
    # Iterate through the given integers
    for i in range(N):
        # Convert the integer to binary
        binary = bin(A[i])[2:]
        
        # Initialize a variable to store the result of the operation
        result = 0
        
        # Iterate through the binary representation of the integer
        for j in range(len(binary)):
            # If the current bit is 1, perform the operation
            if binary[j] == '1':
                # Double the result
                result = result * 2
                
                # Take the XOR of the result and the current integer
                result = result ^ A[i]
                
        # Add the result to the count
        count += result
    
    # Return the count modulo 998244353
    return count % 998244353

if __name__ == '__main__':
    # Read the input from stdin
    input_list = sys.stdin.read().split()
    N = int(input_list[0])
    X = int(input_list[1])
    A = input_list[2:]
    
    # Convert the list of strings to a list of integers
    A = [int(x, 2) for x in A]
    
    # Solve the problem
    print(solve(N, X, A))

