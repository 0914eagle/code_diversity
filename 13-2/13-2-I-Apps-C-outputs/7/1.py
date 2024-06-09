
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
        inspections[name] = order.index(name) + 1

        # Add the current student to the set of inspected students
        inspected.add(name)

    # Return the minimum number of inspections needed and the positions of the students to go back to after each inspection
    return min(inspections.values()), [order.index(name) + 1 for name in inspections]

