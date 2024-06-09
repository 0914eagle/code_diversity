
def solve(queries):
    # Initialize a dictionary to store the students and their knowledge
    students = {}

    # Iterate over the queries
    for query in queries:
        # If the query is a student moving in, add them to the dictionary with their knowledge
        if query.startswith("D"):
            a, b = map(int, query.split()[1:])
            students[len(students) + 1] = (a, b)
        # If the query is a student asking for help, find the student with the most knowledge and return their ID
        elif query.startswith("P"):
            # Find the student with the most knowledge
            max_student = max(students.items(), key=lambda x: x[1][1])
            # If the student cannot be helped, return "NE"
            if max_student[1][0] < students[int(query.split()[1])][0]:
                return "NE"
            # Otherwise, return the ID of the student with the most knowledge
            return max_student[0]

    # If the input is invalid, return "NE"
    return "NE"

