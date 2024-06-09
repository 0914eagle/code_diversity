
import sys

def solve(N, M):
    # Calculate the number of possible toppings combinations
    num_combinations = 2**N
    
    # Initialize a list to store the number of bowls of ramen for each combination
    num_bowls = [0] * num_combinations
    
    # Iterate over each combination and calculate the number of bowls of ramen for that combination
    for i in range(num_combinations):
        # Convert the binary representation of the combination to a list of booleans
        combination = [bool(i & (1 << j)) for j in range(N)]
        
        # Count the number of true values in the list (i.e., the number of toppings chosen for this combination)
        num_toppings = sum(combination)
        
        # If the number of toppings is at least 2, add 1 to the number of bowls of ramen for this combination
        if num_toppings >= 2:
            num_bowls[i] = 1
    
    # Calculate the total number of bowls of ramen by summing the number of bowls for each combination
    total_bowls = sum(num_bowls)
    
    # Return the total number of bowls of ramen modulo M
    return total_bowls % M

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(solve(N, M))

