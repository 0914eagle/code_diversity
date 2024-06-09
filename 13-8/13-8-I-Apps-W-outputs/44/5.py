
def solve(n, p):
    # Initialize a dictionary to map each student to their second hole badge
    badges = {}

    # Iterate through the list of reported students
    for i in range(n):
        # If the student has already been marked with a hole, skip them
        if i in badges:
            continue
        # If the student has not been marked with a hole, mark them with a hole
        badges[i] = 1
        # If the student has a second hole, mark them with a hole
        if i in p:
            badges[i] = 2

    # Return the dictionary of students with two holes in their badges
    return badges

