
def solve(n, k):
    # Initialize a list to store the colors of the costumes
    colors = [0] * n
    
    # Loop through each pair
    for i in range(n):
        # If this is not the first pair, make sure the colors are different from the previous pair
        if i > 0:
            while colors[i-1] == colors[i]:
                colors[i] = random.randint(1, k)
        
        # Make sure the colors are different from each other
        while colors[i] == colors[i-1]:
            colors[i] = random.randint(1, k)
    
    # Return the colors of the costumes
    return "YES\n" + "\n".join([str(colors[i-1]) + " " + str(colors[i]) for i in range(n)])

