
def solve(N, M):
    # Initialize the number of sets to 0
    num_sets = 0
    
    # Iterate over all possible combinations of toppings
    for i in range(2**N):
        # Convert the binary representation of i to a list of 0s and 1s
        toppings = [int(x) for x in bin(i)[2:]]
        
        # Check if the current combination of toppings satisfies the conditions
        if len(set(toppings)) == N and all(toppings.count(1) >= 2):
            num_sets += 1
    
    # Return the number of sets modulo M
    return num_sets % M

