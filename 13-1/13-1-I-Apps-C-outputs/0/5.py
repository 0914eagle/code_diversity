
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
        # Find the class that teacher d teaches on Tuesday of the x-th week
        d, x = query[1], query[2]
        for plan in plans:
            if plan[1] == x:
                # Rotate the teachers in the plan
                teachers = rotate_teachers(teachers, plan[2])
                break
        print(classes[teachers.index(d)])

def rotate_teachers(teachers, plan):
    # Rotate the teachers in the plan
    for i in range(len(plan)):
        teachers[teachers.index(plan[i])] = plan[(i+1) % len(plan)]
    return teachers

