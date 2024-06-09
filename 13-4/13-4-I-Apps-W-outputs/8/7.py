
def solve(n, a, b, places):
    # Initialize the maximum number of students to be 0
    max_students = 0

    # Loop through each possible configuration of students
    for i in range(n + 1):
        # Calculate the number of student-programmers and student-athletes that can be placed in the current configuration
        num_prog = 0
        num_ath = 0
        for j in range(i):
            if places[j] == "A":
                num_prog += 1
            elif places[j] == "B":
                num_ath += 1

        # Check if the current configuration satisfies the conditions
        if num_prog <= a and num_ath <= b:
            # Update the maximum number of students if necessary
            max_students = max(max_students, i)

    return max_students

