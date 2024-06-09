
def get_worst_case_waiting_time(a, b, n, m, roads):
    # Initialize a dictionary to store the shortest distance from each intersection to Janet's house
    distances = {1: 0}
    # Initialize a dictionary to store the previous intersection for each intersection
    previous = {1: None}
    # Loop through each intersection
    for i in range(1, n + 1):
        # If the intersection is not Janet's house, loop through each road
        if i != n:
            for road in roads:
                # If the road starts at the current intersection and the destination is not the previous intersection,
                # and the sum of the distance from the current intersection and the time to travel along the road is less than the current shortest distance,
                # update the shortest distance and the previous intersection
                if road[0] == i and road[1] != previous[i] and distances[i] + road[2] < distances[road[1]]:
                    distances[road[1]] = distances[i] + road[2]
                    previous[road[1]] = i
        # If the intersection is Janet's house, break the loop
        else:
            break
    
    # Initialize a variable to store the worst case waiting time
    worst_case = 0
    # Loop through each intersection
    for i in range(1, n + 1):
        # If the intersection is not Janet's house, and the shortest distance from the intersection to Janet's house is greater than the worst case waiting time,
        # update the worst case waiting time
        if i != n and distances[i] > worst_case:
            worst_case = distances[i]
    
    # Return the worst case waiting time
    return worst_case

