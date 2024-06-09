
def get_class_teacher(teachers, week, day):
    # Find the current week and day
    current_week = week % len(teachers)
    current_day = (day + current_week - 1) % len(teachers[0])
    
    # Return the teacher teaching the class
    return teachers[current_week][current_day]

def rotate_teachers(teachers, week, day, k):
    # Find the current week and day
    current_week = week % len(teachers)
    current_day = (day + current_week - 1) % len(teachers[0])
    
    # Rotate the teachers
    teachers = teachers[k:] + teachers[:k]
    
    # Return the new teachers list
    return teachers

def main():
    # Read the input
    N, M, Q = map(int, input().split())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    
    # Initialize the teachers and classes
    teachers = [[i for i in range(1, N+1)] for _ in range(M)]
    
    # Process the queries
    for query in queries:
        if query[0] == 0:
            # Add a plan to rotate the teachers
            teachers = rotate_teachers(teachers, query[2], query[1], query[1])
        else:
            # Print the class taught by the teacher on Tuesday of the x-th week
            print(get_class_teacher(teachers, query[2], query[1]))

if __name__ == '__main__':
    main()

