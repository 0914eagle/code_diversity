
def can_zax_and_xaz_coexist(m, n, resources):
    # Initialize a set to store the resources available on each island
    island_resources = set()
    for island in resources:
        island_resources.update(island)

    # Check if the number of resources is even
    if len(island_resources) % 2 != 0:
        return "NO"

    # Check if each island has at least one resource
    for island in resources:
        if not island:
            return "NO"

    # Check if each resource is present on at least two islands
    for resource in island_resources:
        count = 0
        for island in resources:
            if resource in island:
                count += 1
        if count < 2:
            return "NO"

    # Check if the Zax and Xaz can coexist
    zax_resources = set()
    xaz_resources = set()
    for resource in island_resources:
        zax_resources.add(resource)
        xaz_resources.add(resource)
    if zax_resources == xaz_resources:
        return "YES"
    else:
        return "NO"

