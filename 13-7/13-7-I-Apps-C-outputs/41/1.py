
def get_maximum_gold(n, m, gold, roads):
    # Initialize a dictionary to store the amount of gold collected by each village
    gold_collected = {i: 0 for i in range(1, n + 1)}
    gold_collected[1] = 0
    
    # Loop through each road
    for road in roads:
        # Get the two villages connected by the road
        village1, village2 = road
        
        # If the bandits have not already visited the first village, they can collect its gold
        if gold_collected[village1] == 0:
            gold_collected[village1] = gold[village1 - 1]
        
        # If the bandits have not already visited the second village, they can collect its gold
        if gold_collected[village2] == 0:
            gold_collected[village2] = gold[village2 - 1]
    
    # Return the maximum amount of gold collected by the bandits
    return max(gold_collected.values())

