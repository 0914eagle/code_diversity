
def can_zax_and_xaz_coexist(m, n, resources):
    # Initialize a set to store the islands that have been populated by the Zax
    zax_islands = set()
    # Initialize a set to store the islands that have been populated by the Xaz
    xaz_islands = set()
    # Initialize a set to store the natural resources that have been collected by the Zax
    zax_resources = set()
    # Initialize a set to store the natural resources that have been collected by the Xaz
    xaz_resources = set()

    for i in range(m):
        # Get the natural resources present on the current island
        island_resources = resources[i]
        # If the current island has not been populated by either the Zax or the Xaz, populate it with the Zax
        if i not in zax_islands and i not in xaz_islands:
            zax_islands.add(i)
        # If the current island has been populated by the Zax, add the natural resources to the set of resources collected by the Zax
        elif i in zax_islands:
            zax_resources.update(island_resources)
        # If the current island has been populated by the Xaz, add the natural resources to the set of resources collected by the Xaz
        elif i in xaz_islands:
            xaz_resources.update(island_resources)

    # If the Zax have collected all $n$ natural resources, return YES
    if len(zax_resources) == n:
        return "YES"
    # If the Xaz have collected all $n$ natural resources, return YES
    if len(xaz_resources) == n:
        return "YES"
    # Otherwise, return NO
    return "NO"

