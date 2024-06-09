
import sys
import math

def solve(n, m, s, t):
    # Initialize the probability of reaching room N from each room
    prob = [0] * (n + 1)
    prob[n] = 1

    # Loop through each passage
    for i in range(m):
        # Get the source and destination rooms of the passage
        source = s[i]
        destination = t[i]

        # Update the probability of reaching room N from the source room
        prob[source] += prob[destination] / 2

        # Update the probability of reaching room N from the destination room
        prob[destination] += prob[source] / 2

    # Calculate the expected number of passages taken to reach room N
    expected = 0
    for i in range(1, n):
        expected += prob[i] * (n - i)

    return expected

if __name__ == '__main__':
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    print(solve(n, m, s, t))

