
def add_reassignment(week, teachers):
    # Add the reassignment plan for the given week and teachers
    pass

def get_teacher_class(teacher, week):
    # Return the class that the teacher will teach on Tuesday of the given week
    pass

if __name__ == '__main__':
    N, M, Q = map(int, input().split())
    queries = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        queries.append(query)

    for query in queries:
        if query[0] == 0:
            add_reassignment(query[1], query[2:])
        else:
            teacher, week = query[1], query[2]
            print(get_teacher_class(teacher, week))

