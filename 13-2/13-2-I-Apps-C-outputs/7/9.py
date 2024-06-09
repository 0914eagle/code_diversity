
def solve(N, M, list, order):
    # Initialize a dictionary to store the number of inspections needed for each student
    inspections = {}

    # Initialize a set to store the names of the students that have been inspected
    inspected = set()

    # Initialize the number of inspections needed
    num_inspections = 0

    # Loop through the list of names
    for name in list:
        # If the name is not in the set of inspected names, add it to the set and increment the number of inspections needed
        if name not in inspected:
            inspections[name] = num_inspections + 1
            inspected.add(name)
            num_inspections += 1

    # Loop through the order of the students
    for i in range(N):
        # If the current student is not in the set of inspected names, add it to the set and increment the number of inspections needed
        if order[i] not in inspected:
            inspections[order[i]] = num_inspections + 1
            inspected.add(order[i])
            num_inspections += 1

    # Return the number of inspections needed and the positions of the students after each inspection
    return num_inspections, [inspections[i] for i in range(1, N + 1)]

