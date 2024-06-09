
def get_unfairness(n):
    # Initialize variables
    unfairness = 0
    prev_rating = 0
    
    # Iterate through the ratings
    for rating in range(1, n+1):
        # Calculate the difference between the current rating and the previous rating
        diff = rating ^ prev_rating
        
        # Add the difference to the unfairness
        unfairness += diff.bit_length()
        
        # Update the previous rating
        prev_rating = rating
    
    # Return the unfairness
    return unfairness

