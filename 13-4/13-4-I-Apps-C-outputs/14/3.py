
def solve(n, e, roads):
    # Initialize a dictionary to store the chains that have been assigned to each city
    chains = {i: set() for i in range(1, n + 1)}
    
    # Initialize a list to store the roads that have been assigned
    assigned_roads = []
    
    # Loop through each road
    for road in roads:
        # If the road has not been assigned yet
        if road not in assigned_roads:
            # Get the cities connected by the road
            city1, city2 = road
            
            # If both cities have at least one chain that has not been assigned yet
            if len(chains[city1]) < 2 and len(chains[city2]) < 2:
                # Assign the first chain to the road
                chains[city1].add(1)
                chains[city2].add(1)
                assigned_roads.append(road)
            # If one city has at least one chain that has not been assigned yet and the other city has no chains that have not been assigned yet
            elif len(chains[city1]) < 2 and len(chains[city2]) == 0:
                # Assign the first chain to the road
                chains[city1].add(1)
                chains[city2].add(1)
                assigned_roads.append(road)
            # If the first city has no chains that have not been assigned yet and the second city has at least one chain that has not been assigned yet
            elif len(chains[city1]) == 0 and len(chains[city2]) < 2:
                # Assign the first chain to the road
                chains[city1].add(1)
                chains[city2].add(1)
                assigned_roads.append(road)
            # If both cities have no chains that have not been assigned yet
            else:
                # Return "0" to indicate that there is no way to fairly assign the roads
                return "0"
    
    # If all roads have been assigned, return the chains that have been assigned to each road
    return [str(chains[city1].pop()) for road in roads for city1, city2 in [road]]

