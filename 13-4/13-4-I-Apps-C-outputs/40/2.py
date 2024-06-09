
# Read input
N, M, Q = map(int, input().split())

# Initialize the classes and teachers
classes = list(range(1, N+1))
teachers = list(range(1, N+1))

# Initialize the current week and the reassignment plans
current_week = 1
plans = []

# Loop through the queries
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:  # Add a reassignment plan
        plans.append((query[1], query[2], query[3:]))
    else:  # Ask a question
        # Find the teacher and the class for the given week
        teacher = query[1]
        week = query[2]
        class_num = 0
        for i in range(len(plans)):
            if plans[i][1] == week:
                class_num = plans[i][2][(teacher-1) % len(plans[i][2])]
                break
        print(class_num)

