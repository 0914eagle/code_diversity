
def solve(n, m, s, a, b, c):
    # Sort the bugs by complexity in ascending order
    sorted_bugs = sorted(enumerate(a), key=lambda x: x[1])

    # Initialize the variables
    students = [(i, b[i], c[i]) for i in range(n)]
    passes = 0
    days = 0
    result = []

    # Iterate through the bugs
    for i, (j, complexity) in sorted_bugs:
        # Find the student with the highest ability level that can fix the current bug
        student = max(students, key=lambda x: x[1])

        # Check if the student has enough ability level to fix the bug
        if student[1] < complexity:
            return "NO"

        # Add the passes for the student
        passes += student[2]

        # Check if the passes exceed the maximum allowed passes
        if passes > s:
            return "NO"

        # Add the student and the bug to the result
        result.append(student[0])
        result.append(i)

        # Remove the student from the list of students
        students.remove(student)

        # Increment the number of days
        days += 1

    # Check if all the bugs were fixed
    if len(result) != m:
        return "NO"

    # Return the result
    return "YES\n" + " ".join(map(str, result))

