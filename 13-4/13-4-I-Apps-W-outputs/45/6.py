
def get_max_sweets(n, s, xy_list):
    # Sort the xy_list in descending order based on the first element of the tuple
    xy_list.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the maximum number of sweets to 0
    max_sweets = 0
    
    # Iterate through the xy_list
    for x, y in xy_list:
        # Check if the current type of sugar is within Caisa's budget
        if x <= s:
            # Calculate the number of sweets that Caisa can get as change
            sweets = (s - x) * 100 + y
            
            # Update the maximum number of sweets if necessary
            max_sweets = max(max_sweets, sweets)
            
            # Break the loop if the maximum number of sweets has been reached
            if max_sweets == 99:
                break
    
    # Return the maximum number of sweets
    return max_sweets

