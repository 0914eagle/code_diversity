
def solve(boat_arrival_times):
    # Initialize variables
    total_time = 0
    bridge_open = True
    queue = []

    # Iterate through each boat arrival time
    for i in range(len(boat_arrival_times)):
        # If the bridge is open, check if the next boat is within 20 seconds of the current time
        if bridge_open and i < len(boat_arrival_times) - 1 and boat_arrival_times[i + 1] - boat_arrival_times[i] <= 20:
            # If the next boat is within 20 seconds, add it to the queue
            queue.append(boat_arrival_times[i + 1])
        # If the bridge is closed or the next boat is not within 20 seconds, close the bridge
        else:
            bridge_open = False
            total_time += 60

        # If the queue is not empty, process the next boat in the queue
        if queue:
            # If the bridge is closed, open it and add the time it takes to raise the bridge
            if not bridge_open:
                bridge_open = True
                total_time += 60

            # Add the time it takes for the boat to pass through the bridge
            total_time += 20

            # If the next boat in the queue is within 20 seconds of the current time, add it to the queue
            if i < len(boat_arrival_times) - 1 and queue[0] - boat_arrival_times[i] <= 20:
                queue.append(queue[0])
                queue.pop(0)

    return total_time

