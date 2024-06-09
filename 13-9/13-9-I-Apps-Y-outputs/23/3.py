
def get_good_observatories(elevations, roads):
    # Initialize a dictionary to store the elevations of the observatories that can be reached from each observatory
    reachable_elevations = {}
    for road in roads:
        observatory1, observatory2 = road
        if observatory1 not in reachable_elevations:
            reachable_elevations[observatory1] = set()
        if observatory2 not in reachable_elevations:
            reachable_elevations[observatory2] = set()
        reachable_elevations[observatory1].add(elevations[observatory2])
        reachable_elevations[observatory2].add(elevations[observatory1])

    # Find the observatories that are good
    good_observatories = []
    for observatory, reachable_elevation in reachable_elevations.items():
        if elevations[observatory] > max(reachable_elevation):
            good_observatories.append(observatory)

    return len(good_observatories)

