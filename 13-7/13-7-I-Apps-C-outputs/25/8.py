
def rotate_teachers(classes, weeks, queries):
    # Initialize a dictionary to store the class assignments for each teacher and week
    class_assignments = {}
    for week in range(1, weeks + 1):
        for teacher in range(1, len(classes) + 1):
            class_assignments[(teacher, week)] = classes[teacher - 1]

    # Process the queries
    for query in queries:
        if query[0] == 0:
            # Add a rotation plan
            teachers = query[1:]
            week = query[2]
            for i in range(len(teachers)):
                teacher = teachers[i]
                class_ = classes[i]
                class_assignments[(teacher, week)] = class_
        else:
            # Ask a question
            teacher = query[1]
            week = query[2]
            print(class_assignments[(teacher, week)])

def main():
    num_classes, num_weeks, num_queries = map(int, input().split())
    classes = list(range(1, num_classes + 1))
    queries = []
    for i in range(num_queries):
        query = list(map(int, input().split()))
        queries.append(query)
    rotate_teachers(classes, num_weeks, queries)

if __name__ == '__main__':
    main()

