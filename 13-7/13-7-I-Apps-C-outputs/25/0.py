
def get_teacher_class(teachers, weeks, query):
    # Initialize a dictionary to store the class assignment for each teacher and week
    class_assignment = {}
    for week in range(1, weeks+1):
        for teacher in teachers:
            class_assignment[(teacher, week)] = teacher

    # Process the queries
    for query in queries:
        if query[0] == 0:
            # Add a reassignment plan
            teachers = query[1:]
            week = query[2]
            for i in range(len(teachers)):
                class_assignment[(teachers[i], week)] = teachers[(i+1) % len(teachers)]
        else:
            # Print the class assignment for a teacher on a particular week
            teacher = query[1]
            week = query[2]
            print(class_assignment[(teacher, week)])

def main():
    N, M, Q = map(int, input().split())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    get_teacher_class(range(1, N+1), M, queries)

if __name__ == '__main__':
    main()

