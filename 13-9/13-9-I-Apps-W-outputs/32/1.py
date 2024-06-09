
def solve(n, k, chips):
    # Initialize the colors of the chips
    colors = [c for c in chips]
    
    # Iterate through each iteration
    for i in range(k):
        # Iterate through each chip
        for j in range(n):
            # Get the colors of the current chip and its two neighbors
            curr_color = colors[j]
            neigh_1 = colors[(j-1)%n]
            neigh_2 = colors[(j+1)%n]
            
            # Check if the current chip should become white
            if neigh_1 == neigh_2 == curr_color:
                colors[j] = "W"
            else:
                colors[j] = "B"
    
    # Return the final colors of the chips
    return "".join(colors)

