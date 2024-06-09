
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

        # Check if the string satisfies the given conditions
        if all(s[i] != s[i+1] for i in range(N-1)):
            num_strings += 1

    # Return the number of strings modulo (10^9+7)
    return num_strings % 1000000007

if __name__ == '__main__':
    N = int(input())
    c_AA = input()
    c_AB = input()
    c_BA = input()
    c_BB = input()
    print(solve(N, c_AA, c_AB, c_BA, c_BB))

