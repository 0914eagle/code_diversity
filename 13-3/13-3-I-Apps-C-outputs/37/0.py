
import sys

def solve(N, M):
    # Calculate the number of possible toppings combinations
    num_combinations = 2**N
    
    # Calculate the number of sets of bowls of ramen that satisfy the conditions
    num_sets = 0
    for i in range(num_combinations):
        # Convert the binary representation of i to a list of 0s and 1s
        binary_rep = list(map(int, list(bin(i)[2:])))
        
        # Count the number of 1s in the binary representation
        num_ones = binary_rep.count(1)
        
        # If the number of 1s is at least 2, add the current combination to the number of sets
        if num_ones >= 2:
            num_sets += 1
    
    # Return the number of sets modulo M
    return num_sets % M

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(solve(N, M))

