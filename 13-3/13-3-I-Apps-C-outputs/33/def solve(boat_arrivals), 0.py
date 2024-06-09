
def solve(boat_arrivals):
    # Initialize variables
    total_time = 0
    bridge_open = True
    queue = []

    # Iterate through each boat arrival
    for i in range(len(boat_arrivals)):
        # If the bridge is open, raise it and add the current boat to the queue
        if bridge_open:
            total_time += 60
            bridge_open = False
            queue.append(boat_arrivals[i])

        # If the bridge is closed, check if the next boat in the queue has arrived
        else:
            # If the next boat has arrived, raise the bridge and add it to the queue
            if queue[0] == boat_arrivals[i]:
                total_time += 60
                bridge_open = False
                queue.append(boat_arrivals[i])

            # If the next boat has not arrived, wait for it to arrive and add it to the queue
            else:
                total_time += 20
                queue.append(boat_arrivals[i])

    # Once all boats have passed, close the bridge
    total_time += 60
    bridge_open = False

    return total_time

