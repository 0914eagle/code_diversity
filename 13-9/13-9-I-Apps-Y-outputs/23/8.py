
import math

def get_manhattan_distance(student, checkpoint):
    return abs(student[0] - checkpoint[0]) + abs(student[1] - checkpoint[1])

def get_nearest_checkpoint(student, checkpoints):
    nearest_distance = math.inf
    nearest_checkpoint = -1
    for checkpoint in checkpoints:
        distance = get_manhattan_distance(student, checkpoint)
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_checkpoint = checkpoint[2]
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
    for nearest_checkpoint in nearest_checkpoints:
        print(nearest_checkpoint)

def read_input():
    student_count, checkpoint_count = map(int, input().split())
    students = []
    for _ in range(student_count):
        students.append(list(map(int, input().split())))
    checkpoints = []
    for _ in range(checkpoint_count):
        checkpoints.append(list(map(int, input().split())) + [i+1] for i in range(checkpoint_count))
    return students, checkpoints

if __name__ == '__main__':
    main()

