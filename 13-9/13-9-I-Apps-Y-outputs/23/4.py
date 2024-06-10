
def get_nearest_checkpoint(student, checkpoints):
    nearest_checkpoint = None
    min_distance = float('inf')
    for checkpoint in checkpoints:
        distance = manhattan_distance(student, checkpoint)
        if distance < min_distance:
            min_distance = distance
            nearest_checkpoint = checkpoint
    return nearest_checkpoint

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def solve(students, checkpoints):
    nearest_checkpoints = []
    for student in students:
        nearest_checkpoint = get_nearest_checkpoint(student, checkpoints)
        nearest_checkpoints.append(nearest_checkpoint)
    return nearest_checkpoints

def main():
    num_students, num_checkpoints = map(int, input().split())
    students = []
    for _ in range(num_students):
        students.append(tuple(map(int, input().split())))
    checkpoints = []
    for _ in range(num_checkpoints):
        checkpoints.append(tuple(map(int, input().split())))
    nearest_checkpoints = solve(students, checkpoints)
    for nearest_checkpoint in nearest_checkpoints:
        print(nearest_checkpoint)

if __name__ == '__main__':
    main()

