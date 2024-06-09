
def f1(N, M, Q):
    # Initialize the classes and teachers
    classes = [i for i in range(1, N+1)]
    teachers = [i for i in range(1, N+1)]
    
    # Initialize the weekly assignments
    weekly_assignments = [[0] * N for _ in range(M)]
    
    # Loop through the queries
    for _ in range(Q):
        # Read the query
        query = input().split()
        
        # Check the type of query
        if query[0] == "0":
            # Add a reassignment plan
            K = int(query[1])
            x = int(query[2])
            plan = query[3:]
            
            # Rotate the teachers
            for i in range(K):
                teacher = plan[i]
                class_num = weekly_assignments[x-1][teacher-1]
                weekly_assignments[x][teacher-1] = class_num
                weekly_assignments[x][plan[i+1]-1] = teacher
        else:
            # Ask a question
            d = int(query[1])
            x = int(query[2])
            print(weekly_assignments[x-1][d-1])
            
def f2(...):
    ...
    
if __name__ == '__main__':
    f1(3, 4, 5)

