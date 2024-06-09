
def min_cost_road_trip(n, g, distances, costs):
    # Initialize the dp table with the cost of the first gas station
    dp = [costs[0]] * (g + 1)
    dp[0] = 0
    
    # Loop through each gas station
    for i in range(1, n):
        # Loop through each possible amount of gas
        for j in range(g, -1, -1):
            # If the current gas station is within reach, calculate the minimum cost to get there
            if distances[i] <= j:
                dp[j] = min(dp[j], dp[j - distances[i]] + costs[i])
            # If the current gas station is out of reach, set the cost to infinity
            else:
                dp[j] = float('inf')
    
    # Return the minimum cost to reach the last gas station
    return "cancel road trip" if dp[g] == float('inf') else dp[g]

