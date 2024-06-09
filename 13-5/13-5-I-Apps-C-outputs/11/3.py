
def solve(n, a, b):
    # Initialize a dictionary to map each statue to its current and desired position
    statue_map = {i: (a[i], b[i]) for i in range(n)}
    
    # Initialize a set to keep track of the empty pedestals
    empty_pedestals = set([i for i in range(n) if a[i] == 0])
    
    # Loop until all the statues are in the desired position
    while True:
        # Check if all the statues are in the desired position
        if all([statue_map[i][0] == statue_map[i][1] for i in range(n)]):
            return "YES"
        
        # Find the empty pedestal with the closest statue
        closest_empty_pedestal = min(empty_pedestals, key=lambda x: abs(x - statue_map[x][0]))
        
        # Find the statue that is closest to the empty pedestal
        closest_statue = min(statue_map, key=lambda x: abs(x - closest_empty_pedestal))
        
        # Move the statue to the empty pedestal
        statue_map[closest_statue] = (closest_empty_pedestal, statue_map[closest_statue][1])
        empty_pedestals.remove(closest_empty_pedestal)
        empty_pedestals.add(closest_statue)
    
    return "NO"

