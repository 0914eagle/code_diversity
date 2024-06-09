
def solve(n, a, b, places):
    # Initialize the maximum number of students to be 0
    max_students = 0

    # Loop through each possible configuration of students
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            # Check if the current configuration is valid
            if is_valid(places, i, j, a, b):
                # Update the maximum number of students if necessary
                max_students = max(max_students, i + j)

    # Return the maximum number of students
    return max_students

# Check if a given configuration is valid
def is_valid(places, i, j, a, b):
    # Initialize the number of student-programmers and student-athletes to be 0
    num_programmers = 0
    num_athletes = 0

    # Loop through each place in the configuration
    for k in range(0, i + j):
        # Check if the current place is occupied by a student-programmer or student-athlete
        if places[k] == "A":
            num_programmers += 1
        elif places[k] == "B":
            num_athletes += 1

    # Check if the number of student-programmers and student-athletes is valid
    return num_programmers == a and num_athletes == b

