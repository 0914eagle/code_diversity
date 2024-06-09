
def solve(n, m, s, a, b, c):
    # Sort the bugs by complexity in descending order
    a.sort(reverse=True)
    # Initialize the number of passes given to each student to 0
    passes = [0] * n
    # Initialize the number of days needed to fix all bugs to 0
    days = 0
    # Iterate through the bugs
    for i in range(m):
        # Find the student with the highest level of ability among the students who have not yet fixed a bug
        student = max(range(n), key=lambda i: b[i])
        # If the student's level of ability is not greater than or equal to the complexity of the current bug, then it cannot be fixed
        if b[student] < a[i]:
            return "NO"
        # Increment the number of passes given to the student
        passes[student] += 1
        # Increment the number of days needed to fix all bugs
        days += 1
        # If the total number of passes given to all students exceeds the maximum number of passes the university is willing to give, then it is not possible to fix all bugs
        if sum(passes) > s:
            return "NO"
    # Return "YES" and the schedule of work
    return "YES\n" + " ".join(str(student + 1) for student in range(n))

