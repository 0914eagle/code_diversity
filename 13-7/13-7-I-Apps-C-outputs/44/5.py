
def solve(n, g, d, e, links):
    # Initialize variables
    alien_system = None
    human_system = None
    min_uw_distance = float('inf')

    # Loop through each system
    for i in range(n):
        # If the system is alien and has the minimum gravity value, set it as the alien system
        if d[i] == 'a' and g[i] < g[alien_system] or alien_system is None:
            alien_system = i

        # If the system is human and has the minimum gravity value, set it as the human system
        if d[i] == 'h' and g[i] < g[human_system] or human_system is None:
            human_system = i

    # Calculate the UW distance between the alien and human systems
    uw_distance = abs(g[alien_system] - g[human_system])

    # If the UW distance is less than the minimum, update the minimum UW distance
    if uw_distance < min_uw_distance:
        min_uw_distance = uw_distance

    # Return the minimum UW distance
    return min_uw_distance

