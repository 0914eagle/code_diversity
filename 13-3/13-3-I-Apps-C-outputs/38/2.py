
def solve(n, star_systems, e, links):
    # Initialize the minimum UW distance to a large value
    min_uw_distance = 1000000
    # Loop through all possible pairs of star systems
    for i in range(n):
        for j in range(i+1, n):
            # If the star systems are of different types, continue
            if star_systems[i][1] != star_systems[j][1]:
                continue
            # Calculate the UW distance between the two star systems
            uw_distance = calculate_uw_distance(star_systems[i][0], star_systems[j][0], links)
            # If the UW distance is less than the minimum, update the minimum
            if uw_distance < min_uw_distance:
                min_uw_distance = uw_distance
    # Return the minimum UW distance
    return min_uw_distance

def calculate_uw_distance(g1, g2, links):
    # Calculate the capacitance, potential, and inductance of the two star systems
    capacitance = g1 + g2
    potential = g1 - g2
    inductance = g1 * g2
    # Initialize the UW distance to the potential times the capacitance
    uw_distance = potential * capacitance
    # Loop through all direct links between the two star systems
    for link in links:
        # If the link is not between the two star systems, continue
        if link[0] != g1 and link[1] != g2:
            continue
        # Calculate the capacitance, potential, and inductance of the link
        link_capacitance = link[0] + link[1]
        link_potential = link[0] - link[1]
        link_inductance = link[0] * link[1]
        # Update the UW distance with the potential times the capacitance of the link
        uw_distance += link_potential * link_capacitance
    # Return the absolute value of the UW distance
    return abs(uw_distance)

def main():
    # Read the input
    n = int(input())
    star_systems = []
    for i in range(n):
        g, d = input().split()
        star_systems.append((int(g), d))
    e = int(input())
    links = []
    for i in range(e):
        link = input().split()
        links.append((int(link[0]), int(link[1])))
    # Solve the problem
    min_uw_distance = solve(n, star_systems, e, links)
    # Print the minimum UW distance
    print(min_uw_distance)

if __name__ == "__main__":
    main()

