
def solve(trips):
    # Initialize variables to keep track of the total cost and the current time
    total_cost = 0
    current_time = 0
    
    # Iterate through each trip
    for trip in trips:
        # Calculate the duration of the trip in minutes
        duration = trip - current_time
        
        # Check if the trip can be covered by a one-trip ticket
        if duration <= 90:
            # Add the cost of the one-trip ticket to the total cost
            total_cost += 20
            
        # Check if the trip can be covered by a 90-minute ticket
        elif duration <= 1440:
            # Calculate the number of 90-minute tickets needed to cover the trip
            num_tickets = duration // 90
            
            # Add the cost of the 90-minute tickets to the total cost
            total_cost += num_tickets * 50
            
        # Check if the trip can be covered by a one-day ticket
        else:
            # Add the cost of the one-day ticket to the total cost
            total_cost += 120
            
        # Update the current time to the end of the trip
        current_time = trip
    
    # Return the total cost
    return total_cost

