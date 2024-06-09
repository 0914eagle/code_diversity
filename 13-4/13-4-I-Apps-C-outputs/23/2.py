
def can_zax_and_xaz_coexist(m, n, islands):
    # Initialize a set to store the resources present on each island
    resources = set()
    
    # Iterate over the islands
    for island in islands:
        # Add the resources present on this island to the set
        resources.update(island)
    
    # Check if the set of resources is equal to the set of all natural resources
    if resources == set(range(1, n + 1)):
        return "YES"
    else:
        return "NO"

