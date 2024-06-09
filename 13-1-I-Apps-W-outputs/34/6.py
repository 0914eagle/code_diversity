
def solve(a, b):
    # Calculate the absolute difference between the two positions
    diff = abs(a - b)
    
    # Initialize the total tiredness to 0
    tiredness = 0
    
    # Loop through the range of the absolute difference
    for i in range(1, diff + 1):
        # Calculate the tiredness for each move
        tiredness += i
    
    # Return the total tiredness
    return tiredness

