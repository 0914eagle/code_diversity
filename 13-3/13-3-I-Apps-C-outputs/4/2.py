
import sys

def solve(N, X, A):
    # Initialize the count of different integers not exceeding X to 0
    count = 0
    
    # Iterate through the given integers A_i
    for i in range(N):
        # Convert the integer A_i to binary
        binary_str = bin(A[i])[2:]
        
        # Initialize a variable to store the current integer
        current_int = 0
        
        # Iterate through the binary representation of A_i
        for j in range(len(binary_str)):
            # If the current bit is 1, add the corresponding power of 2 to the current integer
            if binary_str[j] == "1":
                current_int += 2**j
            
            # If the current integer is not greater than X, increment the count
            if current_int <= X:
                count += 1
    
    # Return the count of different integers not exceeding X
    return count % 998244353

if __name__ == "__main__":
    # Read the input from stdin
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Solve the problem
    print(solve(N, X, A))

