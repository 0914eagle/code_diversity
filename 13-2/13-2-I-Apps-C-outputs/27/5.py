
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
    for i, (bug_index, bug_complexity) in sorted_bugs:
        for j, (student_index, student_ability) in sorted_students:
            # Check if the student's ability is greater than or equal to the bug's complexity
            if student_ability >= bug_complexity:
                # Give the student one pass for fixing the bug
                passes_given[student_index] += 1
                # Increment the number of days needed to fix all bugs
                days_needed += 1
                # Break out of the inner loop to move on to the next bug
                break

    # Check if the total number of passes given exceeds the maximum number of passes the university is willing to give
    if sum(passes_given) > s:
        return "NO"

    # If all bugs are fixed and the total number of passes given does not exceed the maximum, return the schedule of work
    return "YES\n" + " ".join(str(student_index + 1) for student_index, _ in sorted_students)

