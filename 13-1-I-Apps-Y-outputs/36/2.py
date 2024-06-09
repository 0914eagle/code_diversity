
def solve(n, packages):
    # Initialize the shortest path as empty string
    shortest_path = ""

    # Loop through the packages and calculate the minimum number of moves required to collect them
    for package in packages:
        # Calculate the distance between the current package and the robot's position
        distance = abs(package[0]) + abs(package[1])

        # If the distance is even, the robot can move up and right to collect the package
        if distance % 2 == 0:
            shortest_path += "RU" * int(distance / 2)
        # If the distance is odd, the robot can only move right to collect the package
        else:
            shortest_path += "R" * distance

    # Return the shortest path
    return shortest_path

