
def solve(N, M, list, order):
    # Initialize a dictionary to store the number of inspections needed for each student
    inspections = {}

    # Initialize a set to store the names of the students that have been inspected
    inspected = set()

    # Loop through the list of names in descending order
    for name in sorted(list, reverse=True):
        # If the name is not in the set of inspected names, it means it has not been inspected yet
        if name not in inspected:
            # Add the name to the set of inspected names
            inspected.add(name)
            # Get the index of the name in the initial order
            index = order.index(name)
            # If the index is 0, it means the student is at the front of the line and does not need to move
            if index == 0:
                inspections[name] = 0
            # Otherwise, the student needs to move to the front of the line
            else:
                inspections[name] = index

    # Return the minimum number of inspections needed and the positions for each student
    return min(inspections.values()), [order.index(name) for name in sorted(list, reverse=True)]

