
def bridge_operator(arrival_times):
    # Initialize variables
    total_time = 0
    bridge_open = True
    queue = []

    # Iterate through the arrival times
    for arrival_time in arrival_times:
        # If the bridge is open, check if the next boat is arriving soon
        if bridge_open:
            # If the next boat is arriving soon, close the bridge
            if arrival_time - total_time <= 30 * 60:
                bridge_open = False
                total_time += 60
        # If the bridge is closed, check if all boats have passed through
        else:
            # If all boats have passed through, open the bridge
            if not queue:
                bridge_open = True
            # Otherwise, add the current boat to the queue
            else:
                queue.append(arrival_time)

    # Return the total time during which the bridge is unavailable for road traffic
    return total_time

