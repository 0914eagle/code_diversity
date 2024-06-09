
def solve(n, gravity, direct_links, device=False):
    # Initialize the capacitance, potential, and inductance sequences
    capacitance = [0] * n
    potential = [0] * n
    inductance = [0] * n

    # Calculate the capacitance, potential, and inductance for each system
    for i in range(n):
        capacitance[i] = sum(gravity[j] for j in range(i+1, n) if j in direct_links[i])
        potential[i] = sum(gravity[j] for j in range(i+1, n) if j not in direct_links[i])
        inductance[i] = sum(gravity[j] * gravity[k] for j in range(i+1, n) for k in range(j+1, n) if (j, k) in direct_links)

    # Calculate the UW distance for each system
    uw_distance = [0] * n
    for i in range(n):
        uw_distance[i] = abs(potential[i] * (capacitance[i] * capacitance[i] - inductance[i]))

    # If the gravity dispersal device is used, reduce the gravity of the system and increase the gravity of all directly linked systems
    if device:
        for i in range(n):
            gravity[i] -= 1
            for j in direct_links[i]:
                gravity[j] += 1

    # Calculate the minimum UW distance between an alien and human system
    min_distance = float('inf')
    for i in range(n):
        for j in range(n):
            if gravity[i] == 'a' and gravity[j] == 'h':
                min_distance = min(min_distance, uw_distance[i] + uw_distance[j])

    return min_distance

