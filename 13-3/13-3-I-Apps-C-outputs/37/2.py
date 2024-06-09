
import sys

def solve(N, M):
    # Calculate the number of possible combinations of toppings
    num_combinations = 2**N
    
    # Initialize a list to store the number of bowls of ramen for each combination
    num_bowls = [0] * num_combinations
    
    # Iterate over each combination of toppings
    for i in range(num_combinations):
        # Convert the binary representation of the combination to a list of booleans
        combination = [bool(i & (1 << j)) for j in range(N)]
        
        # Count the number of toppings in the combination
        num_toppings = sum(combination)
        
        # If the number of toppings is at least 2, increment the number of bowls for this combination
        if num_toppings >= 2:
            num_bowls[i] += 1
    
    # Calculate the number of unique combinations of bowls of ramen
    num_unique_combinations = len(set(num_bowls))
    
    # Return the number of unique combinations modulo M
    return num_unique_combinations % M

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(solve(N, M))

