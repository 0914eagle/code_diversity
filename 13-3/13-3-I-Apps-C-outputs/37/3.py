
import sys

def solve(N, M):
    # Calculate the number of possible combinations of toppings
    num_combinations = 2**N
    
    # Calculate the number of sets of bowls of ramen that satisfy the conditions
    num_sets = 0
    for i in range(num_combinations):
        # Convert the binary representation of i to a list of booleans, where each boolean represents whether a topping is used or not
        toppings = [bool(i & (1 << j)) for j in range(N)]
        
        # Check if all toppings are used at least twice
        all_toppings_used = True
        for j in range(N):
            if toppings.count(True) < 2:
                all_toppings_used = False
                break
        
        # Check if no toppings are used more than once
        no_duplicate_toppings = True
        for j in range(N):
            if toppings.count(True) > 1:
                no_duplicate_toppings = False
                break
        
        # If all toppings are used at least twice and no toppings are used more than once, increment the number of sets
        if all_toppings_used and no_duplicate_toppings:
            num_sets += 1
    
    # Return the number of sets modulo M
    return num_sets % M

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(solve(N, M))

