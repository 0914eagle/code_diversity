
def get_teacher_assignment(classes, weeks, queries):
    # Initialize a dictionary to store the teacher assignments
    teacher_assignments = {}
    
    # Loop through each week
    for week in range(1, weeks + 1):
        # Loop through each class
        for class_num in range(1, classes + 1):
            # If the week is the first week, assign the teacher to the class
            if week == 1:
                teacher_assignments[class_num] = class_num
            # Otherwise, rotate the teachers
            else:
                current_teacher = teacher_assignments[class_num]
                next_teacher = (current_teacher + 1) % classes
                teacher_assignments[class_num] = next_teacher
    
    # Loop through each query
    for query in queries:
        # If the query is a rotation plan, update the teacher assignments
        if query[0] == 0:
            teachers = query[1:]
            for teacher in teachers:
                teacher_assignments[teacher] = (teacher_assignments[teacher] + 1) % classes
        # If the query is a teacher assignment query, return the class number
        else:
            teacher = query[1]
            week = query[2]
            class_num = teacher_assignments[teacher]
            if week == 1:
                yield class_num
            else:
                yield (class_num + week - 1) % classes

def main():
    classes, weeks, queries = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(queries)]
    for query in get_teacher_assignment(classes, weeks, queries):
        print(query)

if __name__ == '__main__':
    main()

