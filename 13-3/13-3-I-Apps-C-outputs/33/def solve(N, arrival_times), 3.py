
def solve(N, arrival_times):
    # Initialize variables
    total_time = 0
    bridge_open = True
    waiting_boats = []

    # Sort the arrival times in ascending order
    arrival_times.sort()

    # Loop through each boat and simulate the passage of time
    for i in range(N):
        # If the bridge is open, check if the next boat is arriving within the next 20 seconds
        if bridge_open:
            if i < N - 1 and arrival_times[i + 1] - arrival_times[i] <= 20:
                # If the next boat is arriving within the next 20 seconds, close the bridge
                bridge_open = False
                total_time += 60
            else:
                # If the next boat is not arriving within the next 20 seconds, keep the bridge open
                continue
        else:
            # If the bridge is closed, add the current boat to the waiting list
            waiting_boats.append(i)

        # If there are boats waiting and the bridge is closed, open the bridge and let the boats pass through
        if waiting_boats and not bridge_open:
            bridge_open = True
            total_time += 60
            for j in range(len(waiting_boats)):
                total_time += 20
                waiting_boats.pop(0)

    return total_time

