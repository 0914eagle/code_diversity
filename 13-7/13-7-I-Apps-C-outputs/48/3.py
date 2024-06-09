
def solve(n, m, s, a, b, c):
    # Sort the bugs by complexity in descending order
    a.sort(reverse=True)
    # Initialize the number of passes given to each student to 0
    passes = [0] * n
    # Initialize the number of days needed to fix all bugs to 0
    days = 0
    # Loop through the bugs
    for i in range(m):
        # Find the student with the highest level of ability who can fix the current bug
        student = 0
        while student < n and b[student] < a[i]:
            student += 1
        # If no student can fix the current bug, return "NO"
        if student == n:
            return "NO"
        # Increment the number of passes given to the student who fixed the bug
        passes[student] += 1
        # Increment the number of days needed to fix all bugs
        days += 1
    # If the total number of passes exceeds the maximum number of passes given by the university, return "NO"
    if sum(passes) > s:
        return "NO"
    # Return "YES" and the schedule of work
    return "YES\n" + " ".join(str(i + 1) for i in range(n) if passes[i])

