
def solve(N, M, s_list, c_list):
    # Initialize the smallest integer as -1
    smallest_int = -1

    # Iterate through all possible integers with N digits
    for i in range(10**(N-1), 10**N):
        # Convert the integer to a list of digits
        digit_list = list(str(i))

        # Check if the digit at each position is correct
        for j in range(M):
            if digit_list[s_list[j]-1] != str(c_list[j]):
                break
        else:
            # If all digits are correct, update the smallest integer
            smallest_int = i
            break

    # Return the smallest integer
    return smallest_int

