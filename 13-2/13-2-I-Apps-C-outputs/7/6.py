
def solve(N, M, list, order):
    # Initialize a dictionary to store the number of inspections needed for each student
    inspections = {}

    # Initialize a set to store the names of the students that have been inspected
    inspected = set()

    # Initialize the number of inspections needed
    num_inspections = 0

    # Loop through the list of students in order
    for i in range(N):
        # Get the name of the current student
        name = order[i]

        # If the student has not been inspected yet, add them to the set of inspected students
        if name not in inspected:
            inspected.add(name)
            num_inspections += 1

            # If the student is on the list, remove them from the list and add them to the dictionary of inspections
            if name in list:
                list.remove(name)
                inspections[name] = i

    # Loop through the list of students in order again
    for i in range(N):
        # Get the name of the current student
        name = order[i]

        # If the student has not been inspected yet and is on the list, add them to the set of inspected students
        if name not in inspected and name in list:
            inspected.add(name)
            num_inspections += 1
            inspections[name] = i

    # Return the number of inspections needed and the dictionary of inspections
    return num_inspections, inspections

