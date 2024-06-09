
def solve(n, k):
    # Initialize a list to store the colors of the costumes
    colors = [0] * n
    
    # Iterate through the pairs
    for i in range(n):
        # If this is not the first pair, make sure the colors are different from the previous pair
        if i > 0:
            while colors[i-1] == colors[i]:
                colors[i] = random.randint(1, k)
        
        # Make sure the colors are different from each other
        while colors[i] == colors[i-1]:
            colors[i] = random.randint(1, k)
    
    # Check if the colors satisfy the constraints
    for i in range(n-1):
        if colors[i] == colors[i+1] or colors[i] == colors[i-1] or colors[i+1] == colors[i-1]:
            return "NO"
    
    # If all constraints are satisfied, return the colors
    return "YES\n" + "\n".join([str(colors[i]) + " " + str(colors[i+1]) for i in range(n)])

