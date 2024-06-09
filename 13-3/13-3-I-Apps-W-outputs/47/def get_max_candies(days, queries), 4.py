
def get_max_candies(days, queries):
    # Initialize a variable to store the maximum number of candies
    max_candies = 0
    
    # Iterate over the queries
    for query in queries:
        # Initialize a variable to store the minimum number of candies required
        min_candies = query
        
        # Initialize a variable to store the number of candies collected on that day
        collected_candies = 0
        
        # Iterate over the days
        for day in days:
            # If the number of candies collected on that day is greater than or equal to the minimum number of candies required, break the loop
            if collected_candies >= min_candies:
                break
            
            # Add the number of candies collected on that day to the total number of candies collected
            collected_candies += day
        
        # If the total number of candies collected is greater than the maximum number of candies, update the maximum number of candies
        if collected_candies > max_candies:
            max_candies = collected_candies
    
    # Return the maximum number of candies
    return max_candies

