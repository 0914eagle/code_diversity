
def solve(N, M, list, order):
    # Initialize a dictionary to store the number of inspections needed for each student
    inspections = {}

    # Initialize a set to store the names of the students that have been inspected
    inspected = set()

    # Loop through the list of students in the order given
    for i in range(N):
        # Get the name of the current student
        name = order[i]

        # If the student has not been inspected yet, add them to the set of inspected students
        if name not in inspected:
            inspected.add(name)

            # If the student is on the list, add them to the dictionary of inspections
            if name in list:
                inspections[name] = i

    # Loop through the list of students in the order given
    for i in range(N):
        # Get the name of the current student
        name = order[i]

        # If the student has not been inspected yet, add them to the set of inspected students
        if name not in inspected:
            inspected.add(name)

            # If the student is on the list, add them to the dictionary of inspections
            if name in list:
                inspections[name] = i

    # Return the minimum number of inspections needed and the positions of the students to go back to
    return len(inspections), [inspections[name] for name in inspections]

