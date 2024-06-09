
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

        # Increase the student's passes and the number of days needed to fix the bug
        passes[student] += c[student]
        days += 1

    # Check if the university can give the students the required passes
    if sum(passes) <= s:
        return "YES"
    else:
        return "NO"

