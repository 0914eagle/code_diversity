
def solve(n, m, s, a, b, c):
    # Sort the bugs by complexity in descending order
    sorted_bugs = sorted(range(m), key=lambda i: a[i])

    # Initialize the students' passes and the number of days needed to fix the bugs
    students_passes = [0] * n
    days_needed = 0

    # Iterate through the bugs and assign them to the students
    for i in sorted_bugs:
        # Find the student with the highest level of ability who can fix the current bug
        student_idx = max(range(n), key=lambda j: b[j] - a[i])

        # Increment the student's passes and the number of days needed to fix the bug
        students_passes[student_idx] += 1
        days_needed += 1

        # If the student's passes exceed the maximum number of passes, return "NO"
        if students_passes[student_idx] > c[student_idx]:
            return "NO"

    # If the total number of passes exceeds the maximum number of passes, return "NO"
    if sum(students_passes) > s:
        return "NO"

    # Return "YES" and the schedule of work
    return "YES\n" + " ".join(map(str, students_passes))

