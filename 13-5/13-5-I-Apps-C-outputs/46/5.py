
def solve(N, queries):
    # Initialize a dictionary to store the students and their knowledge levels
    students = {}
    
    # Iterate over the queries
    for query in queries:
        # If the query is a student moving in, add them to the dictionary with their knowledge levels
        if query.startswith("D"):
            a, b = map(int, query.split()[1:])
            students[len(students) + 1] = (a, b)
        # If the query is a student asking for help, find the student who can help them
        else:
            i = int(query.split()[1])
            # Initialize the best student to help as None
            best_student = None
            # Initialize the minimum difference in understanding and knowledge quantity as infinity
            min_diff = float("inf")
            # Iterate over the students in the dictionary
            for j, (a, b) in students.items():
                # If the current student has more understanding and knowledge than the querying student, and their difference is less than the minimum difference, update the best student and minimum difference
                if a >= students[i][0] and b >= students[i][1] and (a - students[i][0], b - students[i][1]) < min_diff:
                    best_student = j
                    min_diff = (a - students[i][0], b - students[i][1])
            # If no student can help the querying student, output "NE"
            if best_student is None:
                print("NE")
            # Otherwise, output the best student to help the querying student
            else:
                print(best_student)
    
    return students

