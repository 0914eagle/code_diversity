
import sys

def solve(N, S):
    # Initialize the count of distinct strings to 0
    count = 0

    # Loop through each possible length of the string
    for length in range(1, N+1):
        # Loop through each possible starting index for the string
        for start in range(N-length+1):
            # Extract the substring of length `length` starting at index `start`
            substring = S[start:start+length]

            # Check if the substring is valid (i.e., it does not contain any consecutive characters that are the same)
            if all(substring[i] != substring[i+1] for i in range(length-1)):
                # Increment the count of distinct strings
                count += 1

    # Return the count of distinct strings modulo (10^9+7)
    return count % (10**9+7)

if __name__ == "__main__":
    N = int(input())
    S = input()
    print(solve(N, S))

