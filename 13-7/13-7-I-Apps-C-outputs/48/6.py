
def solve(n, m, s, a, b, c):
    # Sort the bugs by complexity in ascending order
    a.sort()
    # Initialize the number of passes given to each student to 0
    passes = [0] * n
    # Initialize the number of days needed to fix all bugs to 0
    days = 0
    # Loop through each bug
    for i in range(m):
        # Find the student with the highest level of ability who can fix the current bug
        student = max(range(n), key=lambda i: b[i])
        # If the student's level of ability is not greater than or equal to the bug's complexity, break the loop
        if b[student] < a[i]:
            break
        # Increment the number of passes given to the student
        passes[student] += 1
        # Increment the number of days needed to fix all bugs
        days += 1
    # If the total number of passes exceeds the maximum number of passes given by the university, return "NO"
    if sum(passes) > s:
        return "NO"
    # Otherwise, return "YES" and the schedule of work
    return "YES\n" + " ".join(str(student + 1) for student in passes)

