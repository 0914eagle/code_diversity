
# Read input
N, M, Q = map(int, input().split())

# Initialize the class and teacher assignments
classes = list(range(1, N+1))
teachers = list(range(1, N+1))

# Initialize the rotation plans
rotation_plans = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        # Add a rotation plan
        rotation_plans.append((query[1], query[2], query[3:]))
    else:
        # Find the class taught by the teacher on Tuesday of the x-th week
        teacher = query[1]
        week = query[2]
        for rotation in rotation_plans:
            if rotation[1] == week:
                # Find the index of the teacher in the rotation plan
                teacher_index = rotation[2].index(teacher)
                # Find the class where the teacher will be teaching
                class_teacher = rotation[2][(teacher_index + 1) % len(rotation[2])]
                break
        print(classes[class_teacher-1])

