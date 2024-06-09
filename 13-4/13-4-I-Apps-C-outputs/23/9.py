
def can_zax_and_xaz_coexist(m, n, resources):
    # Initialize a set to store the resources found on each island
    resources_on_island = set()
    for island in resources:
        resources_on_island.update(island)

    # Check if there are exactly 2n resources on El-gă-rizm
    if len(resources_on_island) != 2 * n:
        return "NO"

    # Check if each resource is present on exactly 2 islands
    for resource in range(1, n + 1):
        if resource not in resources_on_island:
            return "NO"

    return "YES"

