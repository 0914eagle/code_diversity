
# Read input
N, M, Q = map(int, input().split())

# Initialize the class and teacher assignments
classes = list(range(1, N+1))
teachers = list(range(1, N+1))

# Initialize the reassignment plans
plans = []

# Loop through the queries
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        # Add a reassignment plan
        plans.append(query[1:])
    else:
        # Find the teacher's current class
        teacher = query[1]
        current_class = teachers.index(teacher) + 1
        
        # Find the week number
        week = query[2]
        
        # Find the day of the week
        day = "Tuesday"
        
        # Find the class that the teacher will teach
        if week == 1:
            # If it's the first week, the teacher will teach their current class
            class_to_teach = current_class
        else:
            # If it's not the first week, find the class that the teacher will teach based on the reassignment plans
            for plan in plans:
                if plan[0] == week:
                    # If the week number matches a reassignment plan, find the class that the teacher will teach
                    class_to_teach = plan[plan.index(teacher) - 1]
                    break
        
        # Print the answer
        print(class_to_teach)

