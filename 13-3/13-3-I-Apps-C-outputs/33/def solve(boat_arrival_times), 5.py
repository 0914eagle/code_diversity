
def solve(boat_arrival_times):
    # Initialize variables
    total_time = 0
    bridge_open = True
    waiting_boats = []

    # Sort the boat arrival times in ascending order
    sorted_times = sorted(boat_arrival_times)

    # Iterate through the sorted boat arrival times
    for i in range(len(sorted_times)):
        # Check if the bridge is open
        if bridge_open:
            # If the bridge is open, check if there are any waiting boats
            if waiting_boats:
                # If there are waiting boats, pass the first boat through the bridge
                total_time += 20
                bridge_open = False
            else:
                # If there are no waiting boats, raise the bridge
                total_time += 60
                bridge_open = False
        else:
            # If the bridge is closed, check if the next boat is arriving soon
            if i < len(sorted_times) - 1 and sorted_times[i + 1] - sorted_times[i] <= 30:
                # If the next boat is arriving soon, keep the bridge raised for a little while longer
                total_time += 20
            else:
                # If the next boat is not arriving soon, lower the bridge
                total_time += 60
                bridge_open = True

    return total_time

