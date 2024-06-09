
def solve(boat_arrival_times):
    # Initialize variables
    total_time = 0
    bridge_open = True
    waiting_boats = []

    # Sort the boat arrival times in ascending order
    sorted_arrival_times = sorted(boat_arrival_times)

    # Iterate through the sorted arrival times
    for i in range(len(sorted_arrival_times)):
        # If the bridge is open, check if the next boat is within 20 seconds of the current time
        if bridge_open and sorted_arrival_times[i] - total_time <= 20:
            # If the next boat is within 20 seconds, add it to the waiting boats list
            waiting_boats.append(sorted_arrival_times[i])
        # If the bridge is closed or the next boat is not within 20 seconds, close the bridge
        else:
            bridge_open = False
            total_time += 60

        # If there are waiting boats, process them one by one
        if waiting_boats:
            # Sort the waiting boats in ascending order
            sorted_waiting_boats = sorted(waiting_boats)
            # Iterate through the waiting boats
            for j in range(len(sorted_waiting_boats)):
                # If the next waiting boat is within 20 seconds of the current time, add it to the list of passing boats
                if sorted_waiting_boats[j] - total_time <= 20:
                    total_time += 20
                # If the next waiting boat is not within 20 seconds, break the loop
                else:
                    break
            # Empty the waiting boats list
            waiting_boats = []

    # Return the total time during which the bridge is unavailable for road traffic
    return total_time

