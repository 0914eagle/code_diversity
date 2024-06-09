
def get_maximum_gold(n, m, roads, gold):
    # Initialize a dictionary to store the maximum amount of gold that can be stolen from each village
    max_gold = {i: 0 for i in range(1, n + 1)}
    max_gold[1] = 0
    
    # Loop through each road
    for i in range(m):
        # Get the two villages connected by the road
        village1, village2 = roads[i]
        
        # Update the maximum amount of gold that can be stolen from village1
        max_gold[village1] = max(max_gold[village1], gold[village2] - max_gold[village2])
        
        # Update the maximum amount of gold that can be stolen from village2
        max_gold[village2] = max(max_gold[village2], gold[village1] - max_gold[village1])
    
    # Return the maximum amount of gold that can be stolen from the bandit's home
    return max_gold[1]

