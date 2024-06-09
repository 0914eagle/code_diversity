
import sys

def solve(S):
    # Initialize the number of distinct strings to 1
    distinct_strings = 1
    # Loop through each character in the string
    for i in range(len(S) - 1):
        # If the current character is different from the next character
        if S[i] != S[i + 1]:
            # Replace the current character with the character that is different from both the current and next characters
            S = S[:i] + "ABC"[("ABC".index(S[i]) + 1) % 3] + S[i + 2:]
            # Increment the number of distinct strings
            distinct_strings += 1
    # Return the number of distinct strings modulo (10^9+7)
    return distinct_strings % (10**9 + 7)

if __name__ == "__main__":
    # Read the input string
    S = sys.stdin.readline().strip()
    # Print the result
    print(solve(S))

