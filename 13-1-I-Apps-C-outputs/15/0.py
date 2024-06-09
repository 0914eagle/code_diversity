
def solve(n, g, d, e, links):
    # Initialize the minimum UW distance
    min_uw_distance = float('inf')
    # Loop through each possible pair of systems
    for i in range(n):
        for j in range(i+1, n):
            # If the systems are of different types, continue
            if d[i] != d[j]:
                continue
            # Calculate the UW distance for this pair of systems
            uw_distance = calculate_uw_distance(g[i], g[j], links)
            # Update the minimum UW distance
            min_uw_distance = min(min_uw_distance, uw_distance)
    # Return the minimum UW distance
    return min_uw_distance

def calculate_uw_distance(g1, g2, links):
    # Calculate the capacitance, potential, and inductance for the two systems
    capacitance = g1 + g2
    potential = g1 - g2
    inductance = g1 * g2
    # Calculate the UW distance
    uw_distance = abs(potential * (capacitance * capacitance - inductance))
    # Return the UW distance
    return uw_distance

def main():
    # Read the input
    n, g, d, e, links = read_input()
    # Solve the problem
    min_uw_distance = solve(n, g, d, e, links)
    # Print the output
    print(min_uw_distance)

def read_input():
    # Read the number of star systems
    n = int(input())
    # Initialize the list of gravity values and types
    g = []
    d = []
    # Loop through each star system
    for i in range(n):
        # Read the gravity value and type
        g_i, d_i = map(int, input().split())
        # Add the gravity value and type to the list
        g.append(g_i)
        d.append(d_i)
    # Read the number of direct links
    e = int(input())
    # Initialize the list of direct links
    links = []
    # Loop through each direct link
    for i in range(e):
        # Read the two systems connected by the link
        s1, s2 = map(int, input().split())
        # Add the link to the list
        links.append((s1, s2))
    # Return the input
    return n, g, d, e, links

if __name__ == '__main__':
    main()

