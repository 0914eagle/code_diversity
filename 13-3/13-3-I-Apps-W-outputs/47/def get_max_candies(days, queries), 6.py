
def get_max_candies(days, queries):
    # Initialize a list to store the maximum number of candies collected on each day
    max_candies = [0] * len(days)
    
    # Loop through each day and calculate the maximum number of candies collected on that day
    for i in range(len(days)):
        max_candies[i] = max(max_candies[i-1], days[i])
    
    # Loop through each query and calculate the maximum number of candies collected after the festival ends
    result = []
    for query in queries:
        # Initialize a variable to store the maximum number of candies collected after the festival ends
        max_candies_after_festival = 0
        
        # Loop through each day and calculate the maximum number of candies collected on that day
        for i in range(len(days)):
            # If the number of candies collected on the current day is greater than or equal to the minimum number of candies required by Pelu, add it to the total number of candies collected after the festival ends
            if max_candies[i] >= query:
                max_candies_after_festival += max_candies[i]
        
        # Add the maximum number of candies collected after the festival ends to the result list
        result.append(max_candies_after_festival)
    
    # Return the result list
    return result

