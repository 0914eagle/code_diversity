
def solve_ball_problem(n, k):
    # Initialize a list to store the colors of the costumes
    costumes = []
    
    # Iterate through each pair
    for i in range(n):
        # If this is not the first pair, check that the colors of the previous pair are different
        if i > 0:
            prev_pair = costumes[i-1]
            if prev_pair[0] == prev_pair[1]:
                return "NO"
        
        # Choose a color for the man's costume
        man_color = i % k + 1
        
        # Choose a color for the woman's costume that is different from the man's color
        woman_color = (i + 1) % k + 1
        while woman_color == man_color:
            woman_color = (woman_color + 1) % k + 1
        
        # Add the pair to the list of costumes
        costumes.append([man_color, woman_color])
    
    # If we reach this point, we have found a valid color choosing
    return "YES\n" + "\n".join([str(pair[0]) + " " + str(pair[1]) for pair in costumes])

