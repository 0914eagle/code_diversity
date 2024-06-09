
def solve(n, m, s, a, b, c):
    # Sort the bugs by complexity in descending order
    sorted_bugs = sorted(range(m), key=lambda i: a[i])

    # Initialize the students' passes and the number of days needed to fix the bugs
    passes = [0] * n
    days = 0

    # Iterate through the bugs and assign them to the students
    for i in sorted_bugs:
        # Find the student with the highest level of ability who can fix the current bug
        student = max(range(n), key=lambda j: b[j] - a[i])

        # Increment the student's passes and the number of days needed to fix the bug
        passes[student] += 1
        days += 1

        # If the student's passes exceed the maximum number of passes, return "NO"
        if passes[student] > c[student]:
            return "NO"

    # If all the bugs are fixed and the total number of passes does not exceed the maximum, return "YES" and the assignment of bugs to students
    if days == m and sum(passes) <= s:
        return "YES\n" + " ".join(str(student + 1) for student in sorted(range(n), key=lambda i: passes[i]))

    # Otherwise, return "NO"
    return "NO"

