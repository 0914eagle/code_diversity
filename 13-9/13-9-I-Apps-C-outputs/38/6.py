
def count_ways_to_make_figure_complete(n, d):
    # Initialize the number of ways to make the figure complete to 0
    ways = 0
    
    # Loop over all possible ways to connect the parts
    for i in range(1, n):
        for j in range(i+1, n):
            # Check if the parts are connected by a connecting component
            if d[i] >= 1 and d[j] >= 1:
                # Increment the number of ways to make the figure complete
                ways += 1
    
    # Return the number of ways to make the figure complete modulo 998244353
    return ways % 998244353

