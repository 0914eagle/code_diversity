
def rotate_teachers(classes, teachers, week, rotation):
    # Rotate the teachers as described in the rotation plan
    for i in range(len(rotation)):
        current_teacher = rotation[i]
        next_teacher = rotation[(i + 1) % len(rotation)]
        classes[current_teacher - 1] = classes[next_teacher - 1]
    return classes

def get_class_teacher(classes, teacher):
    # Return the class that the teacher is teaching
    return classes[teacher - 1]

def main():
    # Read the input
    N, M, Q = map(int, input().split())
    classes = list(range(1, N + 1))
    teachers = list(range(1, N + 1))
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 0:
            # Add a rotation plan
            rotation = query[2:]
            classes = rotate_teachers(classes, teachers, query[1], rotation)
        else:
            # Ask a question
            teacher = query[1]
            week = query[2]
            class_teacher = get_class_teacher(classes, teacher)
            print(class_teacher)

if __name__ == '__main__':
    main()

