
def solve(n, gravity, system_type, e, links):
    # Initialize variables
    min_distance = float('inf')
    human_system, alien_system = None, None

    # Iterate over all possible pairs of systems
    for i in range(n):
        for j in range(i+1, n):
            # Check if the systems are of different types
            if system_type[i] != system_type[j]:
                # Calculate the UW distance between the systems
                distance = calculate_distance(gravity[i], gravity[j], links)

                # Check if the distance is less than the minimum distance
                if distance < min_distance:
                    min_distance = distance
                    human_system, alien_system = i, j

    # Return the minimum UW distance and the pair of systems
    return min_distance, (human_system, alien_system)

def calculate_distance(g1, g2, links):
    # Calculate the capacitance, potential, and inductance of the sequence
    capacitance = g1 + g2
    potential = g1 - g2
    inductance = g1 * g2

    # Calculate the UW distance
    distance = abs(potential * (capacitance * capacitance - inductance))

    # Return the UW distance
    return distance

def main():
    # Read the input
    n = int(input())
    gravity = []
    system_type = []
    e = int(input())
    links = []
    for i in range(n):
        g, t = map(int, input().split())
        gravity.append(g)
        system_type.append(t)
    for i in range(e):
        s1, s2 = map(int, input().split())
        links.append((s1, s2))

    # Solve the problem
    min_distance, (human_system, alien_system) = solve(n, gravity, system_type, e, links)

    # Print the output
    print(min_distance)
    print(human_system, alien_system)

if __name__ == '__main__':
    main()

