
def solve(N, queries):
    # Initialize a dictionary to store the students and their knowledge
    students = {}
    
    # Iterate over the queries
    for query in queries:
        # If the query is a student moving in, add them to the dictionary with their knowledge
        if query.startswith("D"):
            A, B = map(int, query.split()[1:])
            students[len(students) + 1] = (A, B)
        # If the query is a student asking for help, find the student with the most knowledge and return their index
        elif query.startswith("P"):
            # Find the student with the most knowledge
            max_A, max_B = max(students.values(), key=lambda x: x[0] * x[1])
            # Return the index of the student with the most knowledge
            print(next(i for i, v in students.items() if v == max_A * max_B))
        else:
            raise ValueError("Invalid query:", query)

