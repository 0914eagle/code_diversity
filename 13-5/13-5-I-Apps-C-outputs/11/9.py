
def is_possible(n, a, b):
    # Initialize a dictionary to map each statue to its current and desired position
    statue_map = {i: (a[i], b[i]) for i in range(n)}
    
    # Initialize a set to keep track of the empty pedestals
    empty_pedestals = set([i for i in range(n) if a[i] == 0])
    
    # Loop until all the statues are in their desired position
    while True:
        # Find the statue that is closest to its desired position
        closest_statue = min(statue_map, key=lambda i: abs(statue_map[i][0] - statue_map[i][1]))
        
        # If the closest statue is already in its desired position, we are done
        if statue_map[closest_statue][0] == statue_map[closest_statue][1]:
            break
        
        # Find the empty pedestal that is closest to the closest statue
        closest_empty_pedestal = min(empty_pedestals, key=lambda i: abs(i - closest_statue))
        
        # Move the closest statue to the empty pedestal
        statue_map[closest_statue] = (closest_empty_pedestal, statue_map[closest_statue][1])
        empty_pedestals.remove(closest_empty_pedestal)
        empty_pedestals.add(closest_statue)
    
    # If all the statues are in their desired position, return "YES", otherwise return "NO"
    return "YES" if all(statue_map[i][0] == statue_map[i][1] for i in range(n)) else "NO"

