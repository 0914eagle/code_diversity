
def get_max_sweets(n, s, x_y_pairs):
    # Sort the x_y_pairs in descending order of x
    x_y_pairs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the maximum number of sweets to 0
    max_sweets = 0
    
    # Iterate through the x_y_pairs
    for x, y in x_y_pairs:
        # Check if the current type of sugar is within Caisa's budget
        if x <= s:
            # Calculate the number of sweets that Caisa can get as change
            sweets = s - x
            
            # Update the maximum number of sweets if necessary
            max_sweets = max(max_sweets, sweets)
            
            # Break the loop if Caisa has enough money to buy the current type of sugar
            break
    
    return max_sweets

