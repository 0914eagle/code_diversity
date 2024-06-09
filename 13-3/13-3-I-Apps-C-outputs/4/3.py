
import sys

def solve(N, X, A):
    # Initialize the count of different integers not exceeding X to 0
    count = 0
    
    # Iterate through the given integers A_1, A_2, ..., A_N
    for i in range(N):
        # Convert the current integer A_i to binary
        binary_i = bin(A[i])[2:]
        
        # Initialize a variable to store the current integer
        current_integer = 0
        
        # Iterate through the binary representation of A_i
        for j in range(len(binary_i)):
            # If the current bit is 1, add the corresponding power of 2 to the current integer
            if binary_i[j] == "1":
                current_integer += 2**j
            
            # If the current integer is not greater than X, increment the count
            if current_integer <= X:
                count += 1
    
    # Return the count of different integers not exceeding X
    return count

if __name__ == "__main__":
    # Read the input from stdin
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Solve the problem
    count = solve(N, X, A)
    
    # Print the count modulo 998244353
    print(count % 998244353)

