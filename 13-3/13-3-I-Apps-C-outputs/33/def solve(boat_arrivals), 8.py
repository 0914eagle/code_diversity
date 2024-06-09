
def solve(boat_arrivals):
    # Initialize variables
    total_time = 0
    bridge_open = True
    queue = []

    # Iterate through the boat arrivals
    for i in range(len(boat_arrivals)):
        # If the bridge is open, check if the next boat is within 20 seconds
        if bridge_open:
            if i < len(boat_arrivals) - 1 and boat_arrivals[i + 1] - boat_arrivals[i] <= 20:
                # Add the boat to the queue
                queue.append(boat_arrivals[i])
            else:
                # Open the bridge
                bridge_open = False
                total_time += 60
        else:
            # If the bridge is closed, check if the next boat is within 30 minutes
            if i < len(boat_arrivals) - 1 and boat_arrivals[i + 1] - boat_arrivals[i] <= 1800:
                # Add the boat to the queue
                queue.append(boat_arrivals[i])
            else:
                # Close the bridge
                bridge_open = True
                total_time += 60
                # Process the queue
                while queue:
                    total_time += 20
                    queue.pop(0)

    return total_time

