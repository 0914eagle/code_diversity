
def solve(boat_arrivals):
    # Initialize variables
    total_time = 0
    bridge_time = 0
    queue = []

    # Iterate through each boat arrival
    for arrival in boat_arrivals:
        # If the bridge is not fully raised, raise it and add the time it takes to raise the bridge to the total time
        if bridge_time < 60:
            total_time += 60 - bridge_time
            bridge_time = 60

        # If the bridge is fully raised, add the time it takes for the boat to pass through the bridge to the total time
        total_time += 20

        # If the next boat is within 20 seconds of the current boat, add the time it takes for the bridge to remain raised to the total time
        if arrival - boat_arrivals[len(queue)] < 20:
            total_time += 20

        # Add the current boat to the queue
        queue.append(arrival)

        # If the queue is not empty and the next boat in the queue is within 30 minutes of the current time, remove the boat from the queue and add the time it takes for the bridge to remain raised to the total time
        while len(queue) > 0 and queue[0] - total_time < 1800:
            total_time += 20
            queue.pop(0)

    return total_time

