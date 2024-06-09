
def solve(n, shortcuts):
    # Initialize the minimum energy required to reach each intersection
    min_energy = [0] * (n + 1)

    # Loop through each shortcut
    for shortcut in shortcuts:
        # Get the starting and ending intersections of the shortcut
        start, end = shortcut[0], shortcut[1]

        # Update the minimum energy required to reach the ending intersection
        min_energy[end] = min(min_energy[end], min_energy[start] + 1)

    # Return the minimum energy required to reach each intersection
    return min_energy

