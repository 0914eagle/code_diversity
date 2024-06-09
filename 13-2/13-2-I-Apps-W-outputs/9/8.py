
import sys
import math

def solve(n, m, s, t):
    # Initialize the probability of reaching room N from each room
    prob = [0] * (n + 1)
    prob[n] = 1

    # Loop through all the passages
    for i in range(m):
        # Get the source and destination rooms of the current passage
        src, dest = s[i] - 1, t[i] - 1

        # Update the probability of reaching room N from the source room
        prob[src] += prob[dest] / 2

        # Update the probability of reaching room N from the destination room
        prob[dest] += prob[src] / 2

    # Return the expected number of passages taken to reach room N
    return sum(prob[1:n])

if __name__ == '__main__':
    n, m = map(int, input().split())
    s, t = [], []
    for i in range(m):
        s.append(int(input()))
        t.append(int(input()))
    print(solve(n, m, s, t))

