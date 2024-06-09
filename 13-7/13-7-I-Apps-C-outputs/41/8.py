
def bandit_gold(n, m, g, roads):
    # Initialize the maximum amount of gold to 0
    max_gold = 0
    # Loop through each road
    for road in roads:
        # Get the two villages connected by the road
        village1, village2 = road
        # If the bandits haven't visited village1 yet
        if village1 not in visited:
            # Add the gold in village1 to the maximum amount of gold
            max_gold += g[village1 - 1]
            # Mark village1 as visited
            visited.add(village1)
        # If the bandits haven't visited village2 yet
        if village2 not in visited:
            # Add the gold in village2 to the maximum amount of gold
            max_gold += g[village2 - 1]
            # Mark village2 as visited
            visited.add(village2)
    # Return the maximum amount of gold
    return max_gold

