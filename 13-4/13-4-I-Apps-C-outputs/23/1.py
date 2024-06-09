
def can_zax_and_xaz_coexist(m, n, resources):
    # Initialize a set to store the unique resources
    unique_resources = set()

    # Iterate over the resources of each island
    for island in resources:
        # Add the resources to the set
        unique_resources.update(island)

    # Check if the set size is equal to the number of resources
    if len(unique_resources) == n:
        return "YES"
    else:
        return "NO"

