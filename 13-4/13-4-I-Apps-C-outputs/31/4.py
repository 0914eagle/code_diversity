
def solve(n, g, d, e, links):
    # Initialize the minimum UW distance
    min_distance = float('inf')
    # Loop through all possible pairs of systems
    for i in range(n):
        for j in range(i+1, n):
            # If the systems are of different types, skip this pair
            if d[i] != d[j]:
                continue
            # Calculate the UW distance for this pair of systems
            distance = calculate_distance(g[i], g[j], links)
            # Update the minimum UW distance
            min_distance = min(min_distance, distance)
    # Return the minimum UW distance
    return min_distance

def calculate_distance(g1, g2, links):
    # Calculate the capacitance, potential, and inductance for this pair of systems
    capacitance = g1 + g2
    potential = g1 - g2
    inductance = g1 * g2
    # Calculate the UW distance for this pair of systems
    distance = abs(potential * (capacitance * capacitance - inductance))
    # Return the UW distance
    return distance

def main():
    # Read the input
    n, g, d, e, links = read_input()
    # Solve the problem
    min_distance = solve(n, g, d, e, links)
    # Print the output
    print(min_distance)

def read_input():
    # Read the number of star systems
    n = int(input())
    # Initialize the lists of gravity values and designations
    g = []
    d = []
    # Loop through the star systems
    for i in range(n):
        # Read the gravity value and designation for this system
        g_i, d_i = input().split()
        # Add the gravity value and designation to the lists
        g.append(int(g_i))
        d.append(d_i)
    # Read the number of direct links
    e = int(input())
    # Initialize the list of direct links
    links = []
    # Loop through the direct links
    for i in range(e):
        # Read the two systems that are directly linked
        s1, s2 = input().split()
        # Add the direct link to the list
        links.append((int(s1), int(s2)))
    # Return the input
    return n, g, d, e, links

if __name__ == '__main__':
    main()

