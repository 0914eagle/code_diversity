
import sys

def solve(N, c_AA, c_AB, c_BA, c_BB):
    # Initialize the number of strings to 0
    num_strings = 0

    # Loop through all possible strings of length N
    for i in range(2**N):
        # Convert the binary representation of i to a string
        s = bin(i)[2:]

        # Pad the string with leading 0s to make it length N
        s = "0" * (N - len(s)) + s

        # Check if the string is valid
        if is_valid(s, c_AA, c_AB, c_BA, c_BB):
            # Increment the number of valid strings
            num_strings += 1

    # Return the number of valid strings
    return num_strings % (10**9 + 7)

def is_valid(s, c_AA, c_AB, c_BA, c_BB):
    # Check if the string is length N
    if len(s) != N:
        return False

    # Check if the string contains only A and B
    for c in s:
        if c not in "AB":
            return False

    # Check if the string contains the correct number of each character
    if s.count("A") != N // 2:
        return False
    if s.count("B") != N // 2:
        return False

    # Check if the string contains the correct number of each pair of characters
    if s.count("AA") != c_AA:
        return False
    if s.count("AB") != c_AB:
        return False
    if s.count("BA") != c_BA:
        return False
    if s.count("BB") != c_BB:
        return False

    # If all checks pass, the string is valid
    return True

# Read the input from stdin
N, c_AA, c_AB, c_BA, c_BB = map(int, input().split())

# Call the solve function and print the result
print(solve(N, c_AA, c_AB, c_BA, c_BB))

