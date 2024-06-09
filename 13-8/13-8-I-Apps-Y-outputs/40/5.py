
def solve(N, M, s_list, c_list):
    # Initialize a variable to store the smallest satisfying integer
    smallest_int = -1

    # Loop through all possible integers with N digits
    for i in range(10**(N-1), 10**N):
        # Convert the integer to a list of digits
        int_list = list(str(i))

        # Check if the integer satisfies the conditions
        if all(int_list[s-1] == c for s, c in zip(s_list, c_list)):
            # If it does, update the smallest satisfying integer
            smallest_int = i
            break

    # Return the smallest satisfying integer
    return smallest_int

