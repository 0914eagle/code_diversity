
def solve(N, M, conditions):
    # Initialize the smallest integer to be the maximum possible value
    smallest_int = 10**N - 1
    # Iterate through all possible integers with N digits
    for i in range(10**(N-1), 10**N):
        # Convert the integer to a list of digits
        digits = [int(digit) for digit in str(i)]
        # Check if the integer satisfies the conditions
        if all(digits[s-1] == c for s, c in conditions):
            # If it satisfies the conditions, update the smallest integer
            smallest_int = min(smallest_int, i)
    # Return the smallest integer or -1 if no integer satisfies the conditions
    return smallest_int if smallest_int != 10**N - 1 else -1

