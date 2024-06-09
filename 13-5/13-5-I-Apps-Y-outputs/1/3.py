
def is_valid_color_choosing(n, k, b, g):
    # Check if there are any two completely identical pairs
    for i in range(n):
        for j in range(i+1, n):
            if b[i] == b[j] and g[i] == g[j]:
                return False
    
    # Check if there is a pair with costumes of the same color
    for i in range(n):
        if b[i] == g[i]:
            return False
    
    # Check if there are any two consecutive pairs with the same color
    for i in range(n-1):
        if b[i] == b[i+1] or g[i] == g[i+1]:
            return False
    
    return True

def solve(n, k):
    # Initialize the arrays for the costume colors
    b = [0] * n
    g = [0] * n
    
    # Loop through each pair and assign a unique color to each dancer
    for i in range(n):
        # Assign a unique color to the man
        b[i] = i % k + 1
        # Assign a unique color to the woman
        g[i] = (i + 1) % k + 1
    
    # Check if the color choosing is valid
    if is_valid_color_choosing(n, k, b, g):
        return "YES\n" + "\n".join([str(b[i]) + " " + str(g[i]) for i in range(n)])
    else:
        return "NO"

