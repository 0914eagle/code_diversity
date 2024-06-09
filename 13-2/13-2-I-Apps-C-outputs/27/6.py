
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
        passes[student] += c[student]
        days += 1

    # Check if the total number of passes exceeds the maximum allowed by the university
    if sum(passes) > s:
        return "NO"

    # Return the schedule of work
    return "YES\n" + " ".join(str(i + 1) for i in sorted(range(n), key=lambda j: passes[j], reverse=True))

