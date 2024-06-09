
def can_zax_and_xaz_coexist(m, n, resources):
    # Initialize a set to store the islands that have been populated by the Zax
    zax_islands = set()
    # Initialize a set to store the islands that have been populated by the Xaz
    xaz_islands = set()
    # Iterate through the list of resources
    for resource in resources:
        # If the resource is present on an island that has been populated by the Zax, add the resource to the set of Zax resources
        if resource in zax_islands:
            zax_resources.add(resource)
        # If the resource is present on an island that has been populated by the Xaz, add the resource to the set of Xaz resources
        elif resource in xaz_islands:
            xaz_resources.add(resource)
        # If the resource is present on an island that has not been populated by either the Zax or the Xaz, add the resource to the set of unpopulated resources
        else:
            unpopulated_resources.add(resource)
    
    # If all $n$ resources have been collected by either the Zax or the Xaz, return YES
    if len(zax_resources) == n or len(xaz_resources) == n:
        return "YES"
    # If there are any unpopulated resources, return NO
    if len(unpopulated_resources) > 0:
        return "NO"
    # If there are no unpopulated resources and all $n$ resources have not been collected, return YES
    return "YES"

