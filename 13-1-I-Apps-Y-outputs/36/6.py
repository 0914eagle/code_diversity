
def solve(n, packages):
    # Initialize the shortest path as empty string
    shortest_path = ""

    # Loop through all packages
    for package in packages:
        # Calculate the distance between the current package and the robot's current position
        distance = abs(package[0]) + abs(package[1])

        # If the distance is even, the robot can move up and right to collect the package
        if distance % 2 == 0:
            # Add "R" to the shortest path
            shortest_path += "R"

        # If the distance is odd, the robot can only move right to collect the package
        else:
            # Add "U" to the shortest path
            shortest_path += "U"

    # Return the shortest path
    return shortest_path

