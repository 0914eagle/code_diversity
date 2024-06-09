
N, M, Q = map(int, input().split())

# Initialize the class and teacher assignments
classes = list(range(1, N+1))
teachers = list(range(1, N+1))

# Initialize the reassignment plans
plans = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        # Add a reassignment plan
        plans.append((query[1], query[2], query[3:]))
    else:
        # Find the class taught by teacher d on Tuesday of the x-th week
        d, x = query[1], query[2]
        for plan in plans:
            if plan[1] == x:
                # Apply the reassignment plan
                teachers = plan[2]
                break
        print(classes[teachers.index(d)])

