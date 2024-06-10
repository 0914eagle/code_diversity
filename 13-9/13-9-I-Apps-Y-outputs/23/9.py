
def get_nearest_checkpoint(student, checkpoints):
    nearest_checkpoint = None
    min_distance = float('inf')
    for checkpoint in checkpoints:
        distance = abs(student[0] - checkpoint[0]) + abs(student[1] - checkpoint[1])
        if distance < min_distance:
            min_distance = distance
            nearest_checkpoint = checkpoint
    return nearest_checkpoint

def get_student_checkpoint_indices(students, checkpoints):
    student_checkpoint_indices = []
    for student in students:
        nearest_checkpoint = get_nearest_checkpoint(student, checkpoints)
        student_checkpoint_indices.append(checkpoints.index(nearest_checkpoint) + 1)
    return student_checkpoint_indices

def main():
    num_students, num_checkpoints = map(int, input().split())
    students = []
    for _ in range(num_students):
        students.append(list(map(int, input().split())))
    checkpoints = []
    for _ in range(num_checkpoints):
        checkpoints.append(list(map(int, input().split())))
    student_checkpoint_indices = get_student_checkpoint_indices(students, checkpoints)
    for index in student_checkpoint_indices:
        print(index)

if __name__ == '__main__':
    main()

