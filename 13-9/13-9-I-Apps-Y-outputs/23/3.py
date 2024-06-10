
def get_manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def get_nearest_checkpoint(student, checkpoints):
    nearest_checkpoint = None
    min_distance = float('inf')
    for checkpoint in checkpoints:
        distance = get_manhattan_distance(student, checkpoint)
        if distance < min_distance:
            min_distance = distance
            nearest_checkpoint = checkpoint
    return nearest_checkpoint

def solve(students, checkpoints):
    nearest_checkpoints = []
    for student in students:
        nearest_checkpoint = get_nearest_checkpoint(student, checkpoints)
        nearest_checkpoints.append(nearest_checkpoint)
    return nearest_checkpoints

def main():
    students, checkpoints = read_input()
    nearest_checkpoints = solve(students, checkpoints)
    print_output(nearest_checkpoints)

def read_input():
    student_count, checkpoint_count = map(int, input().split())
    students = []
    for _ in range(student_count):
        students.append(tuple(map(int, input().split())))
    checkpoints = []
    for _ in range(checkpoint_count):
        checkpoints.append(tuple(map(int, input().split())))
    return students, checkpoints

def print_output(nearest_checkpoints):
    for nearest_checkpoint in nearest_checkpoints:
        print(nearest_checkpoint[0])

if __name__ == '__main__':
    main()

