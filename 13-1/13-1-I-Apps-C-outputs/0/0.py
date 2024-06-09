
N, M, Q = map(int, input().split())

# Initialize the class and teacher assignments
classes = list(range(1, N+1))
teachers = list(range(1, N+1))

# Initialize the weekly assignments
weekly_assignments = [[0] * N for _ in range(M)]

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        # Add a reassignment plan
        K, x, *p = query
        for i in range(K):
            teacher = p[i]
            class_ = classes[teacher-1]
            weekly_assignments[x-1][teacher-1] = class_
            classes[teacher-1] = classes[teacher-1+1]
            classes[teacher-1+1] = class_
    else:
        # Ask a question
        d, x = query
        teacher = d
        for i in range(x-1):
            teacher = weekly_assignments[i][teacher-1]
        print(teacher)

