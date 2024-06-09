
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

    # Return the number of valid strings
    return num_strings % (10**9 + 7)

def is_valid(s, c_AA, c_AB, c_BA, c_BB):
    # Check if the string is length 2 or more
    if len(s) < 2:
        return False

    # Check if the first and last characters are the same
    if s[0] != s[-1]:
        return False

    # Check if the string contains only A and B
    for c in s:
        if c not in ['A', 'B']:
            return False

    # Check if the string contains only the given characters
    if c_AA not in ['A', 'B'] or c_AB not in ['A', 'B'] or c_BA not in ['A', 'B'] or c_BB not in ['A', 'B']:
        return False

    # Check if the string contains only the given characters
    if c_AA not in s or c_AB not in s or c_BA not in s or c_BB not in s:
        return False

    # Check if the string is valid
    if s.count(c_AA) % 2 == 1 or s.count(c_AB) % 2 == 1 or s.count(c_BA) % 2 == 1 or s.count(c_BB) % 2 == 1:
        return False

    # If all checks pass, the string is valid
    return True

if __name__ == '__main__':
    N = int(input())
    c_AA = input()
    c_AB = input()
    c_BA = input()
    c_BB = input()
    print(solve(N, c_AA, c_AB, c_BA, c_BB))

