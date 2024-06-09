
def solve(n, systems, links):
    # Initialize the minimum UW distance to a large value
    min_distance = 1000000
    # Loop through all possible pairs of systems
    for i in range(n):
        for j in range(i+1, n):
            # If the systems are of different types, calculate the UW distance
            if systems[i][1] != systems[j][1]:
                distance = calculate_distance(systems[i][0], systems[j][0], links)
                # Update the minimum UW distance if necessary
                if distance < min_distance:
                    min_distance = distance
    return min_distance

def calculate_distance(system1, system2, links):
    # Initialize the UW distance to 0
    distance = 0
    # Loop through all the links between the two systems
    for link in links:
        # If the link is between the two systems, calculate the UW distance for that link
        if (link[0] == system1 and link[1] == system2) or (link[0] == system2 and link[1] == system1):
            distance += calculate_link_distance(system1, system2, link)
    return distance

def calculate_link_distance(system1, system2, link):
    # Initialize the UW distance for the link to 0
    distance = 0
    # If the link is a direct link, calculate the UW distance for the link
    if link[0] == system1 and link[1] == system2:
        distance = abs(system1.gravity - system2.gravity) * (abs(system1.gravity * system2.gravity) - abs(system1.gravity + system2.gravity))
    # If the link is an indirect link, calculate the UW distance for the link by summing the UW distances for all the intermediate systems
    else:
        intermediate_systems = get_intermediate_systems(link, system1, system2)
        for intermediate_system in intermediate_systems:
            distance += abs(intermediate_system.gravity - system1.gravity) * (abs(intermediate_system.gravity * system1.gravity) - abs(intermediate_system.gravity + system1.gravity))
    return distance

def get_intermediate_systems(link, system1, system2):
    # Initialize a list to store the intermediate systems
    intermediate_systems = []
    # If the link is a direct link, return an empty list
    if link[0] == system1 and link[1] == system2:
        return intermediate_systems
    # If the link is an indirect link, find the intermediate systems by traversing the link
    else:
        current_system = system1
        while current_system != system2:
            intermediate_systems.append(current_system)
            current_system = get_next_system(link, current_system)
        return intermediate_systems

def get_next_system(link, current_system):
    # If the current system is the first system in the link, return the second system in the link
    if current_system == link[0]:
        return link[1]
    # If the current system is the second system in the link, return the first system in the link
    elif current_system == link[1]:
        return link[0]
    # If the current system is not in the link, return None
    else:
        return None

# Test the code with the sample input
n = 9
systems = [(377, 'a'), (455, 'h'), (180, 'a'), (211, 'a'), (134, 'a'), (46, 'h'), (111, 'h'), (213, 'h'), (17, 'a')]
links = [(1, 2), (1, 4), (1, 6), (2, 3), (2, 4), (2, 5), (3, 5), (4, 6), (4, 7), (4, 9), (5, 7), (5, 8), (6, 9), (7, 9), (7, 8)]
print(solve(n, systems, links))

