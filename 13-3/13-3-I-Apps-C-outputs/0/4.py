
import sys

def solve(N, c_AA, c_AB, c_BA, c_BB):
    # Initialize the number of strings to 0
    num_strings = 0

    # Loop through all possible strings of length N
    for i in range(1 << N):
        # Convert the binary representation of i to a string
        s = bin(i)[2:]

        # Pad the string with zeros on the left to make it length N
        s = '0' * (N - len(s)) + s

        # Check if the string is valid
        if is_valid(s, c_AA, c_AB, c_BA, c_BB):
            # Increment the number of valid strings
            num_strings += 1

    # Return the number of valid strings modulo (10^9+7)
    return num_strings % (10**9 + 7)

def is_valid(s, c_AA, c_AB, c_BA, c_BB):
    # Check if the string is length N
    if len(s) != N:
        return False

    # Check if the string contains only A and B
    for c in s:
        if c not in ['A', 'B']:
            return False

    # Check if the string is valid according to the rules
    for i in range(N - 1):
        # Check if the i-th and (i+1)-th characters are A and A
        if s[i] == 'A' and s[i+1] == 'A' and s[i] != c_AA:
            return False

        # Check if the i-th and (i+1)-th characters are A and B
        if s[i] == 'A' and s[i+1] == 'B' and s[i] != c_AB:
            return False

        # Check if the i-th and (i+1)-th characters are B and A
        if s[i] == 'B' and s[i+1] == 'A' and s[i] != c_BA:
            return False

        # Check if the i-th and (i+1)-th characters are B and B
        if s[i] == 'B' and s[i+1] == 'B' and s[i] != c_BB:
            return False

    # If all checks pass, the string is valid
    return True

if __name__ == '__main__':
    N, c_AA, c_AB, c_BA, c_BB = map(str, input().split())
    print(solve(int(N), c_AA, c_AB, c_BA, c_BB))

