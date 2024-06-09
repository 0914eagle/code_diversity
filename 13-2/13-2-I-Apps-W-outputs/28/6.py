
def get_maximum_profit(n, h, m, restrictions):
    # Initialize a list to store the height of each house
    heights = [0] * (n + 1)
    
    # Loop through each restriction and update the height of the houses within that restriction
    for l, r, x in restrictions:
        for i in range(l, r + 1):
            heights[i] = min(heights[i], x)
    
    # Calculate the profit by summing the squares of the heights of all the houses
    profit = sum(x**2 for x in heights)
    
    return profit

