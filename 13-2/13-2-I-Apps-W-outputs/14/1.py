
def solve(n, A, dice):
    # Initialize the number of values for each dice
    num_values = [0] * n
    
    # Iterate over each dice
    for i in range(n):
        # Get the maximum value that the current dice can show
        max_value = dice[i]
        
        # Iterate over each value from 1 to the maximum value
        for value in range(1, max_value + 1):
            # Check if the current value is possible for the current dice
            if value <= A:
                # If the current value is possible, then it is guaranteed that the current dice couldn't show it
                num_values[i] += 1
    
    return num_values

