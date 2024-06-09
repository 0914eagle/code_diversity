
def solve(n, m, s, a, b, c):
    # Sort the bugs and students by complexity and level respectively
    sorted_a = sorted(zip(a, range(m)))
    sorted_b = sorted(zip(b, range(n)))

    # Initialize the variables
    passes = 0
    days = 0
    students = []
    bugs = []

    # Iterate through the sorted bugs and students
    for i in range(m):
        for j in range(n):
            # Check if the student can fix the bug
            if sorted_b[j][0] >= sorted_a[i][0]:
                # Add the student to the list of students who can fix the bug
                students.append(sorted_b[j][1])
                # Add the bug to the list of bugs to be fixed
                bugs.append(sorted_a[i][1])
                # Increment the number of passes for the student
                passes += c[sorted_b[j][1]]
                # Increment the number of days to fix the bug
                days += 1

                # Check if the number of passes exceeds the maximum allowed
                if passes > s:
                    return "NO"

    # Check if all bugs have been fixed
    if len(bugs) == m:
        return "YES\n" + " ".join(map(str, students))
    else:
        return "NO"

