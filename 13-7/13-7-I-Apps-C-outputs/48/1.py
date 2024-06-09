
def solve(n, m, s, a, b, c):
    # Sort the bugs by complexity in descending order
    sorted_bugs = sorted(range(m), key=lambda i: a[i])

    # Initialize the students' passes and the number of days needed to fix the bugs
    passes = [0] * n
    days = 0

    # Iterate through the sorted bugs
    for i in sorted_bugs:
        # Find the student with the highest level of ability who can fix the current bug
        student = max(range(n), key=lambda i: b[i])

        # Check if the student has enough passes to fix the bug
        if passes[student] + c[student] >= a[i]:
            # Subtract the complexity of the bug from the student's passes
            passes[student] -= a[i]
        else:
            # The student does not have enough passes, so they cannot fix the bug
            return "NO"

        # Increment the number of days needed to fix the bug
        days += 1

    # Check if the university has enough passes to give to the students
    if sum(passes) <= s:
        return "YES"
    else:
        return "NO"

