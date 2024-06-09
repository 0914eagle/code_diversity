
def solve(boat_arrival_times):
    # Initialize variables
    total_time = 0
    bridge_open = True
    queue = []

    # Iterate through the arrival times of the boats
    for arrival_time in boat_arrival_times:
        # If the bridge is open, check if the next boat has arrived within the next 20 seconds
        if bridge_open:
            if arrival_time - total_time <= 20:
                # If the next boat has arrived, add it to the queue and continue
                queue.append(arrival_time)
                continue
            else:
                # If the next boat has not arrived, close the bridge
                bridge_open = False
                total_time += 60

        # If the bridge is closed, check if the next boat has arrived within the next 20 seconds
        else:
            if arrival_time - total_time <= 20:
                # If the next boat has arrived, add it to the queue and continue
                queue.append(arrival_time)
                continue
            else:
                # If the next boat has not arrived, open the bridge
                bridge_open = True
                total_time += 60

        # If the queue is not empty, process the boats in the queue
        while queue:
            # Get the next boat in the queue
            next_boat = queue.pop(0)

            # Check if the next boat has arrived within the next 20 seconds
            if next_boat - total_time <= 20:
                # If the next boat has arrived, continue processing the queue
                queue.append(next_boat)
                continue
            else:
                # If the next boat has not arrived, close the bridge
                bridge_open = False
                total_time += 60
                break

    return total_time

