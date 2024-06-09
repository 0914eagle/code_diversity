
import sys

def solve(N, c_AA, c_AB, c_BA, c_BB):
    # Initialize the number of strings to 0
    num_strings = 0

    # Loop through all possible strings of length N
    for i in range(2**N):
        # Convert the binary representation of i to a string
        s = bin(i)[2:]

        # Pad the string with zeros if it is not long enough
        s = s.zfill(N)

        # Initialize a flag to indicate if the string is valid
        valid = True

        # Loop through each character in the string
        for j in range(N-1):
            # If the characters at position j and j+1 are both A, check if c_AA is allowed
            if s[j] == "A" and s[j+1] == "A":
                if c_AA == "A":
                    valid = False
                    break
            # If the characters at position j and j+1 are both B, check if c_BB is allowed
            elif s[j] == "B" and s[j+1] == "B":
                if c_BB == "B":
                    valid = False
                    break
            # If the characters at position j and j+1 are A and B, check if c_AB is allowed
            elif s[j] == "A" and s[j+1] == "B":
                if c_AB == "A":
                    valid = False
                    break
            # If the characters at position j and j+1 are B and A, check if c_BA is allowed
            elif s[j] == "B" and s[j+1] == "A":
                if c_BA == "B":
                    valid = False
                    break

        # If the string is valid, increment the number of strings
        if valid:
            num_strings += 1

    # Return the number of strings modulo 10^9+7
    return num_strings % 1000000007

# Read the input from stdin
N, c_AA, c_AB, c_BA, c_BB = input().split()

# Solve the problem
result = solve(int(N), c_AA, c_AB, c_BA, c_BB)

# Print the result
print(result)

