
def solve(n, m, s, a, b, c):
    # Sort the bugs by complexity in ascending order
    sorted_bugs = sorted(enumerate(a), key=lambda x: x[1])

    # Sort the students by their ability level in descending order
    sorted_students = sorted(enumerate(b), key=lambda x: x[1], reverse=True)

    # Initialize the passes given to each student to 0
    passes_given = [0] * n

    # Initialize the number of days needed to fix all bugs to 0
    days_needed = 0

    # Iterate through the sorted bugs and students
    for bug, complexity in sorted_bugs:
        for student, ability in sorted_students:
            # Check if the student's ability is greater than or equal to the bug's complexity
            if ability >= complexity:
                # Increment the number of days needed to fix the bug
                days_needed += 1
                # Increment the passes given to the student
                passes_given[student] += 1
                # Break out of the inner loop to move on to the next bug
                break

    # Check if the total passes given do not exceed the maximum passes given by the university
    if sum(passes_given) <= s:
        # Return the list of students who will fix each bug in the optimal order
        return ["YES"] + [student + 1 for student in sorted(passes_given, key=passes_given.index)]
    else:
        # Return "NO" if the total passes given exceed the maximum passes given by the university
        return ["NO"]

