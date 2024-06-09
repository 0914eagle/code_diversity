
def get_max_gold(n, m, gold, roads):
    # Initialize a dictionary to store the amount of gold in each village
    village_gold = {i: gold[i-1] for i in range(1, n+1)}
    
    # Initialize a set to store the visited villages
    visited = set()
    
    # Initialize a variable to store the maximum amount of gold collected
    max_gold = 0
    
    # Loop through each road
    for a, b in roads:
        # If the villages are not visited yet, visit them and add the gold to the total
        if a not in visited and b not in visited:
            max_gold += village_gold[a] + village_gold[b]
            visited.add(a)
            visited.add(b)
    
    # Return the maximum amount of gold collected
    return max_gold

