
import sys

def get_input():
    n, m = map(int, input().split())
    switches = [[] for _ in range(n+1)]
    bulbs = [0] * (m+1)
    for i in range(1, n+1):
        k, *switches[i] = map(int, input().split())
    for i in range(1, m+1):
        p, = map(int, input().split())
        bulbs[i] = p
    return n, m, switches, bulbs

def count_combinations(n, m, switches, bulbs):
    # Initialize a 2D array to store the number of combinations for each bulb
    dp = [[0] * 2 for _ in range(m+1)]
    # Initialize the number of combinations for the first bulb
    dp[1][0] = 1
    dp[1][1] = 1
    # Loop through the bulbs
    for i in range(2, m+1):
        # Loop through the switches connected to the current bulb
        for j in switches[i]:
            # Add the number of combinations for the current switch to the number of combinations for the current bulb
            dp[i][0] += dp[j][1]
            dp[i][1] += dp[j][0]
        # If the current bulb is lighted when an odd number of switches are "on", subtract the number of combinations where an even number of switches are "on"
        if bulbs[i] == 1:
            dp[i][0] -= dp[i][1]
    # Return the number of combinations for the last bulb
    return dp[m][0]

n, m, switches, bulbs = get_input()
print(count_combinations(n, m, switches, bulbs))

