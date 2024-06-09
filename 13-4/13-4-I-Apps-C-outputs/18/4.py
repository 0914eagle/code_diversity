
import sys
input = sys.stdin.read()

def solve(n, m, tunnels):
    # Initialize the danger level of each chamber as 0
    danger_level = [0] * (n + 1)

    # Loop through each tunnel
    for a, b, length in tunnels:
        # Update the danger level of chamber a
        danger_level[a] += length
        # Update the danger level of chamber b
        danger_level[b] += length

    # Return the remainder of each danger level divided by 10^9 + 7
    return [d % (10**9 + 7) for d in danger_level]

n, m = map(int, input.split())
tunnels = []
for i in range(m):
    a, b, length = map(int, input.split())
    tunnels.append((a, b, length))
print(*solve(n, m, tunnels))

