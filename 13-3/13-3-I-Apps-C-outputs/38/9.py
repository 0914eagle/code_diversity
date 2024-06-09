
def solve(n, gravity, type, links):
    # Initialize variables
    human_system, alien_system = None, None
    min_uw_distance = float('inf')

    # Loop through all possible pairs of star systems
    for i in range(n):
        for j in range(i+1, n):
            # Check if the systems are of different types
            if type[i] != type[j]:
                # Calculate the UW distance between the systems
                uw_distance = calculate_uw_distance(gravity[i], gravity[j], links)

                # Check if the UW distance is less than the minimum distance
                if uw_distance < min_uw_distance:
                    # Update the minimum UW distance and the corresponding star systems
                    min_uw_distance = uw_distance
                    human_system, alien_system = i, j

    # Return the minimum UW distance and the corresponding star systems
    return min_uw_distance, human_system, alien_system

def calculate_uw_distance(gravity1, gravity2, links):
    # Initialize variables
    capacitance, potential, inductance = 0, 0, 0

    # Calculate the capacitance, potential, and inductance between the two systems
    for link in links:
        if link[0] == gravity1 and link[1] == gravity2:
            capacitance += 1
            potential += 1
            inductance += 1
        elif link[0] == gravity2 and link[1] == gravity1:
            capacitance += 1
            potential -= 1
            inductance -= 1

    # Calculate the UW distance
    uw_distance = abs(potential * (capacitance * capacitance - inductance))

    # Return the UW distance
    return uw_distance

def main():
    # Read the input
    n = int(input())
    gravity = []
    type = []
    links = []
    for i in range(n):
        g, t = input().split()
        gravity.append(int(g))
        type.append(t)
    e = int(input())
    for i in range(e):
        link = input().split()
        links.append([int(link[0]), int(link[1])])

    # Solve the problem
    min_uw_distance, human_system, alien_system = solve(n, gravity, type, links)

    # Print the output
    print(min_uw_distance)

if __name__ == '__main__':
    main()

