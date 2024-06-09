
def solve(n, packages):
    # Initialize the shortest path as empty string
    shortest_path = ""

    # Loop through the packages and calculate the minimum number of moves required to collect them
    for package in packages:
        # Calculate the distance between the current package and the robot's position
        distance = abs(package[0]) + abs(package[1])

        # If the distance is even, the robot can move up and right to collect the package
        if distance % 2 == 0:
            # Add the appropriate number of "U"s and "R"s to the shortest path
            shortest_path += "U" * int(distance / 2) + "R" * int(distance / 2)
        # If the distance is odd, the robot can only move up to collect the package
        else:
            # Add the appropriate number of "U"s to the shortest path
            shortest_path += "U" * int((distance - 1) / 2) + "R" * int((distance - 1) / 2 + 1)

    # Return the shortest path
    return shortest_path

