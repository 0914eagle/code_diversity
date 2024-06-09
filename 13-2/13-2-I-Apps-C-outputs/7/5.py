
def solve(N, M, list, order):
    # Initialize a dictionary to store the number of inspections needed for each student
    inspections = {}

    # Initialize a set to store the names of the students that have been inspected
    inspected = set()

    # Loop through the list of names and calculate the number of inspections needed for each student
    for name in list:
        # If the student has already been inspected, skip them
        if name in inspected:
            continue

        # Calculate the number of inspections needed for the current student
        inspections[name] = N - order.index(name)

        # Add the current student to the set of inspected students
        inspected.add(name)

    # Sort the dictionary by value in descending order (i.e. number of inspections needed)
    sorted_inspections = sorted(inspections.items(), key=lambda x: x[1], reverse=True)

    # Initialize a list to store the positions of the students in the line after each inspection
    positions = []

    # Loop through the sorted dictionary and calculate the positions of the students in the line after each inspection
    for name, inspections in sorted_inspections:
        # Calculate the position of the student in the line after the current inspection
        position = order.index(name) + inspections

        # Add the position to the list of positions
        positions.append(position)

    # Return the number of inspections needed and the list of positions
    return len(inspections), positions

