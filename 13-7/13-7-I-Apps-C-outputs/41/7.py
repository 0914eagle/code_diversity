
def get_maximum_gold(n, m, gold, roads):
    # Initialize a dictionary to store the amount of gold in each village
    gold_dict = {i: gold[i-1] for i in range(1, n+1)}
    
    # Initialize a set to store the visited villages
    visited = set()
    
    # Initialize a variable to store the maximum amount of gold collected
    max_gold = 0
    
    # Loop through each road
    for a, b in roads:
        # If both villages have not been visited yet
        if a not in visited and b not in visited:
            # Add the gold in the current village to the maximum gold collected
            max_gold += gold_dict[a]
            max_gold += gold_dict[b]
            # Add both villages to the visited set
            visited.add(a)
            visited.add(b)
    
    # Return the maximum amount of gold collected
    return max_gold

