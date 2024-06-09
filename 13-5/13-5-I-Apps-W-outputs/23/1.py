
def solve(trips):
    # Initialize variables to keep track of the total cost and the current time
    total_cost = 0
    current_time = 0
    
    # Iterate through each trip
    for trip in trips:
        # Calculate the cost of the trip based on the time of day
        if trip - current_time <= 90:
            cost = 20
        elif trip - current_time <= 1440:
            cost = 50
        else:
            cost = 120
        
        # Update the total cost and current time
        total_cost += cost
        current_time = trip
        
    # Return the total cost
    return total_cost

