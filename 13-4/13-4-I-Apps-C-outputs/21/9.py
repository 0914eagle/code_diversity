
def f1(N, M, Q):
    # Initialize the class and teacher assignments
    classes = [i for i in range(1, N+1)]
    teachers = [i for i in range(1, N+1)]
    
    # Initialize the weekly assignments
    weekly_assignments = [[0] * N for _ in range(M)]
    
    # Process the queries
    for _ in range(Q):
        query = input().split()
        if query[0] == "0":
            # Add a reassignment plan
            K = int(query[1])
            x = int(query[2])
            plan = [int(i) for i in query[3:]]
            weekly_assignments[x-1] = plan
        else:
            # Ask for a teacher's assignment
            d = int(query[1])
            x = int(query[2])
            print(weekly_assignments[x-1][d-1])
            
def f2(...):
    ...
    
if __name__ == '__main__':
    N, M, Q = map(int, input().split())
    f1(N, M, Q)

