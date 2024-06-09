
import sys

def solve(N, S):
    # Initialize the count of distinct strings to 0
    count = 0

    # Loop through each substring of length N-1 in S
    for i in range(N-1):
        # If the substring is not already in the count, increment the count
        if S[i:i+N-1] not in count:
            count += 1

    # Return the count modulo (10^9+7)
    return count % (10**9+7)

if __name__ == '__main__':
    N = int(input())
    S = input()
    print(solve(N, S))

