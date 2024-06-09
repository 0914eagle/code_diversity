
def bandit_gold(n, m, g, roads):
    # Initialize the maximum amount of gold to 0
    max_gold = 0
    # Loop through each village
    for i in range(1, n+1):
        # If the village is not the bandit's home or the king's castle
        if i != 1 and i != 2:
            # Add the amount of gold in the village to the maximum amount of gold
            max_gold += g[i-1]
    # Return the maximum amount of gold
    return max_gold

