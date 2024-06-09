
def solve(n, m, s, a, b, c):
    # Sort the bugs by complexity in descending order
    sorted_bugs = sorted(range(m), key=lambda i: a[i])

    # Initialize the variables
    students = [0] * n
    passes = 0
    days = 0

    # Loop through the bugs
    for i in sorted_bugs:
        # Find the student with the highest level of ability
        student = max(range(n), key=lambda i: b[i])

        # Check if the student has enough ability to fix the bug
        if b[student] < a[i]:
            return "NO"

        # Assign the bug to the student
        students[student] += 1
        passes += c[student]
        days += 1

        # Check if the passes exceed the maximum allowed by the university
        if passes > s:
            return "NO"

    # Return the answer
    return "YES"

