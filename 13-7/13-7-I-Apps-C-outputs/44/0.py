
def solve(n, systems, links, use_gravity_dispersal):
    # Initialize the minimum UW distance to a large value
    min_distance = float('inf')
    
    # Loop through all possible pairs of systems
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the UW distance between the two systems
            distance = calculate_uw_distance(systems, links, i, j, use_gravity_dispersal)
            
            # Check if the distance is less than the minimum distance
            if distance < min_distance:
                min_distance = distance
    
    # Return the minimum UW distance
    return min_distance

def calculate_uw_distance(systems, links, i, j, use_gravity_dispersal):
    # Initialize the UW distance to 0
    distance = 0
    
    # Loop through all systems in the path between the two systems
    for k in range(i, j):
        # Calculate the capacitance, potential, and inductance of the current system
        capacitance, potential, inductance = calculate_characteristics(systems, links, k)
        
        # Add the potential of the current system to the UW distance
        distance += potential
        
        # If the gravity dispersal device is used, increase the gravity of the current system and all directly linked systems
        if use_gravity_dispersal:
            systems[k] += 1
            for l in links[k]:
                systems[l] += 1
    
    # Return the absolute value of the UW distance
    return abs(distance)

def calculate_characteristics(systems, links, k):
    # Initialize the capacitance, potential, and inductance to 0
    capacitance, potential, inductance = 0, 0, 0
    
    # Loop through all directly linked systems
    for l in links[k]:
        # Calculate the capacitance, potential, and inductance of the current system
        capacitance += systems[l]
        potential += systems[l] - systems[k]
        inductance += systems[l] * systems[k]
    
    # Return the capacitance, potential, and inductance
    return capacitance, potential, inductance

