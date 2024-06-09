
def solve_color_choosing(n, k):
    # Initialize a list to store the colors of the costumes
    colors = []
    
    # Loop through each pair
    for i in range(n):
        # If this is not the first pair, make sure the colors of the previous pair are different
        if i > 0:
            prev_pair = colors[i-1]
            if prev_pair[0] == prev_pair[1]:
                return "NO"
        
        # Choose a color for the man's costume
        man_color = i % k + 1
        
        # Choose a color for the woman's costume that is different from the man's color
        woman_color = (man_color + 1) % k + 1
        
        # Add the pair to the list of colors
        colors.append([man_color, woman_color])
    
    # If we reach this point, we have found a suitable color choosing
    return "YES\n" + "\n".join([str(pair[0]) + " " + str(pair[1]) for pair in colors])

