
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

        # If the student has not been inspected yet, inspect them
        if name not in inspected:
            # Increment the number of inspections needed
            num_inspections += 1

            # Add the student to the set of inspected students
            inspected.add(name)

            # If the student is on the list, strike their name from the list
            if name in list:
                list.remove(name)

            # If the list is empty, break the loop
            if not list:
                break

        # Get the position of the current student in the line
        position = order.index(name)

        # Add the position of the current student to the dictionary of inspections
        inspections[name] = position

    # Return the number of inspections needed and the dictionary of inspections
    return num_inspections, inspections

