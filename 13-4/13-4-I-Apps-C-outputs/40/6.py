
# read the input
N, M, Q = map(int, input().split())

# initialize the class and teacher assignments
classes = list(range(1, N+1))
teachers = list(range(1, N+1))

# dictionary to store the class assignments for each teacher
teacher_classes = {teacher: class_ for teacher, class_ in zip(teachers, classes)}

# dictionary to store the teacher assignments for each class
class_teachers = {class_: teacher for teacher, class_ in zip(teachers, classes)}

# loop through the queries
for _ in range(Q):
    query = input().split()
    if query[0] == "0":
        # add a reassignment plan
        K = int(query[1])
        x = int(query[2])
        plan = tuple(map(int, query[3:]))
        # rotate the teachers
        for i in range(K):
            teacher = plan[i]
            class_ = teacher_classes[teacher]
            teacher_classes[teacher] = class_teachers[class_]
            class_teachers[class_] = teacher
    else:
        # ask a question
        d = int(query[1])
        x = int(query[2])
        print(teacher_classes[d])

