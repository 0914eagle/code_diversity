
def solve(N, queries):
    # Initialize a dictionary to store the students and their knowledge levels
    students = {}
    
    # Iterate over the queries
    for query in queries:
        # If the query is a student moving in, add them to the dictionary with their knowledge levels
        if query.startswith("D"):
            A, B = map(int, query.split()[1:])
            students[len(students) + 1] = (A, B)
        # If the query is a student asking for help, find the student who can help them and output their name
        elif query.startswith("P"):
            i = int(query.split()[1])
            # Find the student with the highest knowledge level who is less than or equal to the student asking for help
            for j in range(i, len(students) + 1):
                if students[j][0] >= students[i][0] and students[j][1] >= students[i][1]:
                    print(j)
                    break
            else:
                print("NE")

