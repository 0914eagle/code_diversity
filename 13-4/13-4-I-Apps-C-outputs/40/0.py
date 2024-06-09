
N, M, Q = map(int, input().split())

# Initialize the class and teacher assignments
classes = [i for i in range(1, N+1)]
teachers = [i for i in range(1, N+1)]

# Initialize the weekly rotation plans
rotation_plans = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        # Add a rotation plan
        rotation_plans.append((query[1], query[2], query[3:]))
    else:
        # Find the class that teacher d teaches on Tuesday of the x-th week
        d, x = query[1], query[2]
        class_assignment = teachers[d-1]
        for rotation in rotation_plans:
            if rotation[0] <= x <= rotation[1]:
                class_assignment = (class_assignment - 1) % N + 1
        print(class_assignment)

