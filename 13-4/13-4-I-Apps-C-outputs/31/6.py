
def solve(n, g, d, e, links):
    # Initialize the minimum UW distance
    min_distance = float('inf')
    # Loop through each possible pair of systems
    for i in range(n):
        for j in range(i+1, n):
            # If the systems are of different types, continue
            if d[i] != d[j]:
                continue
            # Calculate the UW distance for this pair of systems
            distance = calculate_distance(g[i], g[j], links)
            # Update the minimum UW distance
            min_distance = min(min_distance, distance)
    # Return the minimum UW distance
    return min_distance

def calculate_distance(g1, g2, links):
    # Calculate the capacitance, potential, and inductance
    capacitance = g2 + g1
    potential = g2 - g1
    inductance = g2 * g1
    # Calculate the UW distance
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
    # Initialize the gravity values and types
    g = [0] * n
    d = [0] * n
    # Loop through each star system
    for i in range(n):
        # Read the gravity value and type
        g[i], d[i] = map(int, input().split())
    # Read the number of direct links
    e = int(input())
    # Initialize the links
    links = []
    # Loop through each direct link
    for i in range(e):
        # Read the two systems that are directly linked
        links.append(list(map(int, input().split())))
    # Return the input
    return n, g, d, e, links

if __name__ == '__main__':
    main()

