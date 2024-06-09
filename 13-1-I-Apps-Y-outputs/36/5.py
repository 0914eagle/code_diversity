
def solve(n, packages):
    # Initialize the shortest path as empty string
    shortest_path = ""

    # Loop through all packages
    for package in packages:
        # Calculate the distance between the current package and the robot's current position
        distance = abs(package[0]) + abs(package[1])

        # If the distance is even, add one "U" to the shortest path
        if distance % 2 == 0:
            shortest_path += "U"

        # If the distance is odd, add one "R" to the shortest path
        else:
            shortest_path += "R"

    # Return the shortest path
    return shortest_path

