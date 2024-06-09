
def solve(n, m, k, a, b, c, u, v):
    # Initialize the maximum score and the current army size
    max_score = 0
    army_size = k
    
    # Loop through each castle in order
    for i in range(n):
        # Check if the army size is greater than or equal to the number of warriors required to capture the current castle
        if army_size >= a[i]:
            # Add the importance value of the current castle to the maximum score
            max_score += c[i]
            # Subtract the number of warriors required to capture the current castle from the army size
            army_size -= a[i]
            # Hire warriors from the current castle and add them to the army size
            army_size += b[i]
        # If the army size is less than the number of warriors required to capture the current castle, return -1
        else:
            return -1
    
    # Return the maximum score
    return max_score

