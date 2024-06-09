
def get_good_observatories(elevations, roads):
    # Initialize a dictionary to store the elevation of each observatory and whether it is good or not
    observatories = {}
    for i in range(len(elevations)):
        observatories[i+1] = (elevations[i], False)

    # Iterate over the roads and update the elevation and good status of the observatories
    for road in roads:
        observatory1, observatory2 = road
        elevation1, is_good1 = observatories[observatory1]
        elevation2, is_good2 = observatories[observatory2]
        if elevation1 > elevation2:
            observatories[observatory2] = (elevation1, True)
        elif elevation2 > elevation1:
            observatories[observatory1] = (elevation2, True)

    # Count the number of good observatories
    count = 0
    for observatory in observatories.values():
        if observatory[1]:
            count += 1

    return count

