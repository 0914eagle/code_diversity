
def add_plan(N, M, K, x, plan):
    # Add the plan to the list of plans
    plans.append((x, plan))

    # Rotate the teachers according to the plan
    for i in range(K):
        current_class = classes[plan[i] - 1]
        next_class = classes[(plan[i] + 1) % N]
        classes[plan[i] - 1] = next_class
        classes[(plan[i] + 1) % N] = current_class

def get_teacher_class(d, x):
    # Find the teacher's current class
    for i in range(len(plans)):
        if plans[i][0] == x:
            break
    current_class = classes[plans[i][1][d - 1] - 1]
    return current_class

N, M, Q = map(int, input().split())
classes = list(range(1, N + 1))
plans = []

for i in range(Q):
    query = input().split()
    if query[0] == "0":
        add_plan(N, M, int(query[1]), int(query[2]), list(map(int, query[3:])))
    else:
        print(get_teacher_class(int(query[1]), int(query[2])))


