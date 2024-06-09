
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
        for i in range(len(plans)):
            if plans[i][1] == x:
                # Find the index of teacher d in the plan
                idx = plans[i][2].index(d)
                # Return the class that teacher d will teach on Tuesday
                print(plans[i][2][(idx+1)%len(plans[i][2])])
                break
        else:
            # If there is no reassignment plan for the week x, return the current class
            print(d)

