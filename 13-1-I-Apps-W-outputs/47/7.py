
def solve(n, m, k, a, b, c, u, v):
    # Initialize the maximum score and the current army size
    max_score = 0
    army_size = k
    
    # Loop through each castle in order
    for i in range(n):
        # Check if the army size is enough to capture the current castle
        if army_size >= a[i]:
            # Capture the castle and add its importance value to the score
            max_score += c[i]
            # Hire warriors from the castle and add them to the army size
            army_size += b[i]
        else:
            # If the army size is not enough, break the loop and return -1
            return -1
    
    # Return the maximum score
    return max_score

