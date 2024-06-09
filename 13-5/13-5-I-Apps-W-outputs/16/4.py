
def solve(cows_per_day, number_of_farms, days):
    # Initialize a list to store the number of farms that need inspection
    farms_to_inspect = []
    
    # Loop through each day
    for day in range(1, days+1):
        # Initialize a variable to store the total number of farms that need inspection
        total_farms = 0
        
        # Loop through each farm
        for i in range(number_of_farms):
            # Check if the farm has at least one cow
            if cows_per_day[i] > 0:
                # Calculate the number of farms that need inspection on this day
                farms_to_inspect.append(cows_per_day[i])
                total_farms += 1
        
        # Print the number of farms that need inspection on this day
        print(total_farms)
    
    # Return the list of farms that need inspection
    return farms_to_inspect

