
import sys

def solve(N, c_AA, c_AB, c_BA, c_BB):
    # Initialize the number of strings to 0
    num_strings = 0

    # Loop through all possible strings of length N
    for i in range(1 << N):
        # Convert the binary representation of i to a string
        s = bin(i)[2:]

        # Pad the string with leading 0s to make it length N
        s = '0' * (N - len(s)) + s

        # Check if the string is valid
        if is_valid(s, c_AA, c_AB, c_BA, c_BB):
            # Increment the number of valid strings
            num_strings += 1

    # Return the number of valid strings modulo (10^9+7)
    return num_strings % 1000000007

def is_valid(s, c_AA, c_AB, c_BA, c_BB):
    # Check if the string is length N
    if len(s) != N:
        return False

    # Check if the string contains only A and B
    for c in s:
        if c not in 'AB':
            return False

    # Check if the string is valid according to the rules
    for i in range(N - 1):
        if s[i] == 'A' and s[i + 1] == 'A' and c_AA not in s:
            return False
        if s[i] == 'A' and s[i + 1] == 'B' and c_AB not in s:
            return False
        if s[i] == 'B' and s[i + 1] == 'A' and c_BA not in s:
            return False
        if s[i] == 'B' and s[i + 1] == 'B' and c_BB not in s:
            return False

    # If all checks pass, the string is valid
    return True

# Read the input from stdin
N, c_AA, c_AB, c_BA, c_BB = input().split()

# Convert the input to integers
N = int(N)

# Convert the input to characters
c_AA = chr(int(c_AA))
c_AB = chr(int(c_AB))
c_BA = chr(int(c_BA))
c_BB = chr(int(c_BB))

# Solve the problem
result = solve(N, c_AA, c_AB, c_BA, c_BB)

# Print the result
print(result)

