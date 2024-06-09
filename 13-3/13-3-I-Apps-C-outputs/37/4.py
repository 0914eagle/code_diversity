
def solve(N, M):
    # Initialize the number of possible combinations to 0
    num_combinations = 0

    # Iterate over all possible combinations of toppings
    for i in range(1, 2**N):
        # Convert the binary representation of i to a list of booleans
        toppings = [bool(i & (1 << j)) for j in range(N)]

        # Check if the current combination of toppings satisfies the conditions
        if all(toppings) and len(set(toppings)) == N:
            num_combinations += 1

    # Return the number of possible combinations modulo M
    return num_combinations % M

