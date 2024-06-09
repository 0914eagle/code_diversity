
def solve(boat_arrivals):
    # Initialize variables
    total_time = 0
    bridge_open = True
    queue = []

    # Iterate through the boat arrivals
    for i in range(len(boat_arrivals)):
        # If the bridge is open, check if the next boat is arriving soon
        if bridge_open:
            # If the next boat is arriving soon, close the bridge
            if i < len(boat_arrivals) - 1 and boat_arrivals[i + 1] - boat_arrivals[i] <= 30 * 60:
                bridge_open = False
                total_time += 60
        
        # If the bridge is closed, check if all boats have passed through
        else:
            # If all boats have passed through, open the bridge
            if not queue:
                bridge_open = True
        
        # Add the current boat to the queue if the bridge is closed
        if not bridge_open:
            queue.append(boat_arrivals[i])
        
        # Simulate the passage of time for the current boat
        total_time += 20
    
    # Return the total time during which the bridge is unavailable for road traffic
    return total_time

