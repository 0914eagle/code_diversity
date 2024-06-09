
def solve(N, queries):
    # Initialize a dictionary to store the students and their knowledge
    students = {}

    # Iterate over the queries
    for query in queries:
        # If the query is a student moving in, add them to the dictionary
        if query.startswith("D"):
            A, B = map(int, query.split()[1:])
            students[len(students) + 1] = (A, B)
        # If the query is a student asking for help, find the student to help them
        elif query.startswith("P"):
            i = int(query.split()[1])
            # Find the student with the highest knowledge quantity and understanding
            # that is greater than or equal to the student's knowledge
            best_student = None
            for j, (A_j, B_j) in students.items():
                if A_j >= students[i][0] and B_j >= students[i][1]:
                    if best_student is None or B_j > students[best_student][1]:
                        best_student = j
            # If no student can be helped, output "NE"
            if best_student is None:
                print("NE")
            # Otherwise, output the name of the student to help
            else:
                print(best_student)

    return students

