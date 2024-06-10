
def rotate_teachers(teachers, classes, plan):
    
    new_teachers = []
    for teacher, class_ in zip(teachers, classes):
        new_teachers.append((teacher, class_))
    for teacher, class_ in plan:
        new_teachers[teacher-1] = (teacher, class_)
    return new_teachers

def get_teacher_class(teachers, week, day):
    
    for teacher, class_ in teachers:
        if teacher.week == week and teacher.day == day:
            return class_
    return None

def get_teacher_classes(teachers, week):
    
    classes = []
    for teacher, class_ in teachers:
        if teacher.week == week:
            classes.append(class_)
    return classes

def main():
    N, M, Q = map(int, input().split())
    teachers = [(i, i) for i in range(1, N+1)]
    classes = list(range(1, N+1))
    plans = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 0:
            plans.append((query[1], query[2], query[3:]))
        else:
            teacher = query[1]
            week = query[2]
            day = query[3]
            classes = get_teacher_classes(teachers, week)
            for class_ in classes:
                if get_teacher_class(teachers, week, day) == class_:
                    print(class_)
                    break

if __name__ == '__main__':
    main()

