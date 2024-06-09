
def get_good_observatories(elevations, roads):
    # Initialize a dictionary to store the elevations of the observatories that can be reached from each observatory
    reachable_elevations = {}
    for road in roads:
        observatory1, observatory2 = road
        if observatory1 not in reachable_elevations:
            reachable_elevations[observatory1] = set()
        reachable_elevations[observatory1].add(elevations[observatory2])
        if observatory2 not in reachable_elevations:
            reachable_elevations[observatory2] = set()
        reachable_elevations[observatory2].add(elevations[observatory1])
    
    # Find the highest elevation that can be reached from each observatory
    highest_elevations = {}
    for observatory, reachable_elevation in reachable_elevations.items():
        highest_elevations[observatory] = max(reachable_elevation)
    
    # Count the number of observatories with an elevation higher than the highest elevation that can be reached from it
    good_observatories = 0
    for observatory, elevation in elevations.items():
        if elevation > highest_elevations[observatory]:
            good_observatories += 1
    
    return good_observatories

