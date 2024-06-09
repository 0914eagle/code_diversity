
def solve(n, m, s, a, b, c):
    # Sort the bugs by complexity in ascending order
    a.sort()
    # Initialize the number of passes given to each student to 0
    passes = [0] * n
    # Initialize the number of days needed to fix all bugs to 0
    days = 0
    # Loop through the bugs
    for i in range(m):
        # Find the student with the highest level of ability among those who can fix the current bug
        student = max(range(n), key=lambda i: b[i] - a[i])
        # Increment the number of passes given to the selected student
        passes[student] += 1
        # Increment the number of days needed to fix all bugs
        days += 1
        # If the total number of passes given exceeds the maximum allowed, return "NO"
        if sum(passes) > s:
            return "NO"
    # If all bugs are fixed, return "YES" and the schedule of work
    return "YES\n" + " ".join(map(str, passes))

