
def solve(N, queries):
    # Initialize a dictionary to store the students and their knowledge
    students = {}

    # Iterate over the queries
    for query in queries:
        # If the query is a student moving in, add them to the dictionary
        if query.startswith("D"):
            A, B = map(int, query.split()[1:])
            students[len(students) + 1] = (A, B)
        # If the query is a student asking for help, find the best student to ask
        elif query.startswith("P"):
            i = int(query.split()[1])
            # Find the student with the highest understanding who is better than the current student
            best_student = None
            for j, (A, B) in students.items():
                if A > students[i][0] and B > students[i][1]:
                    best_student = j
                    break
            # If no student is better, output "NE"
            if best_student is None:
                print("NE")
            # Otherwise, output the best student's ID
            else:
                print(best_student)

    return students

