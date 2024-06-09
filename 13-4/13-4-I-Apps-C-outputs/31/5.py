
def solve(n, gravity, type, links):
    # Initialize variables
    alien_systems = []
    human_systems = []
    system_pairs = []
    system_distances = {}
    gravity_dispersion_devices = 0

    # Populate alien and human systems lists
    for i in range(n):
        if type[i] == "a":
            alien_systems.append(i)
        elif type[i] == "h":
            human_systems.append(i)

    # Populate system pairs and distances dictionary
    for i in range(len(links)):
        system_pairs.append((links[i][0], links[i][1]))
        system_distances[(links[i][0], links[i][1])] = abs(gravity[links[i][0]] - gravity[links[i][1]])

    # Calculate minimum distance using brute force approach
    min_distance = float("inf")
    for alien_system in alien_systems:
        for human_system in human_systems:
            distance = 0
            current_system = alien_system
            while current_system != human_system:
                if (current_system, human_system) in system_pairs:
                    distance += system_distances[(current_system, human_system)]
                    break
                else:
                    distance += system_distances[(current_system, links[current_system])]
                    current_system = links[current_system]
            if distance < min_distance:
                min_distance = distance

    # Account for gravity dispersion devices
    if gravity_dispersion_devices > 0:
        min_distance -= gravity_dispersion_devices

    return min_distance

