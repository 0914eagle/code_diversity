
def solve(N, M, list, order):
    # Initialize a dictionary to store the number of inspections needed for each student
    inspections = {}

    # Initialize a set to store the names of the students that have been inspected
    inspected = set()

    # Initialize the number of inspections needed
    num_inspections = 0

    # Loop through the list of students in the order they appear in the line
    for i in range(N):
        # If the student has not been inspected yet, inspect them
        if i not in inspected:
            num_inspections += 1
            inspected.add(i)

            # If the student's name is on the list, strike it
            if order[i] in list:
                list.remove(order[i])

            # If the list is empty, break the loop
            if not list:
                break

            # Move the student to the back of the line
            order.append(order.pop(0))

    # Return the number of inspections needed and the order of the students in the line after the inspections
    return num_inspections, order

