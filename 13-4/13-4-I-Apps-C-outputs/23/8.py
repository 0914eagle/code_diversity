
def can_zax_and_xaz_coexist(m, n, resources):
    # Initialize a set to store the islands that the Zax have occupied
    zax_islands = set()
    # Initialize a set to store the islands that the Xaz have occupied
    xaz_islands = set()
    # Initialize a set to store the natural resources that the Zax have
    zax_resources = set()
    # Initialize a set to store the natural resources that the Xaz have
    xaz_resources = set()

    for i in range(m):
        # Get the natural resources present on the current island
        island_resources = resources[i]
        # If the island has no resources, skip it
        if not island_resources:
            continue
        # If the island has resources, add it to the appropriate set
        if island_resources[0] in zax_resources:
            xaz_islands.add(i)
        else:
            zax_islands.add(i)
            zax_resources.add(island_resources[0])

    # Check if the Zax have access to all natural resources
    if len(zax_resources) == n:
        return "YES"
    # Check if the Xaz have access to all natural resources
    if len(xaz_resources) == n:
        return "YES"
    # Check if the Zax and Xaz have occupied the same island
    if len(zax_islands & xaz_islands) > 0:
        return "NO"
    # Otherwise, the Zax and Xaz can coexist
    return "YES"

