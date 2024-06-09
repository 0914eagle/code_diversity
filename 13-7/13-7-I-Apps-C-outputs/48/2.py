
def solve(n, m, s, a, b, c):
    # Sort the bugs by complexity in ascending order
    a.sort()
    # Initialize the passes given to each student to 0
    given_passes = [0] * n
    # Initialize the number of days needed to fix all bugs to 0
    days_needed = 0
    # Initialize the list of students who will fix each bug
    bug_fixers = [0] * m
    # Loop through each bug
    for i in range(m):
        # Find the student with the highest level of ability who can fix the current bug
        for j in range(n):
            if b[j] >= a[i]:
                # Assign the current bug to the current student
                bug_fixers[i] = j
                # Increment the number of passes given to the current student
                given_passes[j] += c[j]
                # Increment the number of days needed to fix all bugs
                days_needed += 1
                break
    # Check if the total number of passes given exceeds the maximum number of passes the university is ready to give
    if sum(given_passes) > s:
        return "NO"
    # Return "YES" and the list of students who will fix each bug if the university can fix all bugs within the given time frame
    return "YES\n" + " ".join(map(str, bug_fixers))

