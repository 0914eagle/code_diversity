
def get_good_observatories(n, m, heights, roads):
    # Initialize a dictionary to store the elevation of each observatory
    observatories = {i: heights[i-1] for i in range(1, n+1)}
    # Initialize a dictionary to store the roads that connect each observatory
    roads_dict = {i: set() for i in range(1, n+1)}
    for road in roads:
        roads_dict[road[0]].add(road[1])
        roads_dict[road[1]].add(road[0])
    
    # Initialize a set to store the good observatories
    good_observatories = set()
    
    # Iterate through each observatory
    for observatory in observatories:
        # Initialize a set to store the elevations of the observatories that can be reached from the current observatory
        reachable_elevations = set()
        # Initialize a queue to store the observatories that need to be visited
        queue = [observatory]
        while queue:
            current_observatory = queue.pop(0)
            reachable_elevations.add(observatories[current_observatory])
            for connected_observatory in roads_dict[current_observatory]:
                if connected_observatory not in reachable_elevations:
                    queue.append(connected_observatory)
        
        # If the elevation of the current observatory is higher than all the reachable elevations, it is a good observatory
        if observatories[observatory] > max(reachable_elevations):
            good_observatories.add(observatory)
    
    return len(good_observatories)

