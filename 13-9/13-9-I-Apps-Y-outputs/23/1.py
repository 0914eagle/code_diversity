
import math

def get_manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def get_nearest_checkpoint(student, checkpoints):
    nearest_checkpoint = None
    min_distance = math.inf
    for checkpoint in checkpoints:
        distance = get_manhattan_distance(student, checkpoint)
        if distance < min_distance:
            min_distance = distance
            nearest_checkpoint = checkpoint
    return nearest_checkpoint

def solve(students, checkpoints):
    nearest_checkpoints = []
    for student in students:
        nearest_checkpoints.append(get_nearest_checkpoint(student, checkpoints))
    return nearest_checkpoints

def main():
    students = []
    checkpoints = []
    n, m = map(int, input().split())
    for _ in range(n):
        students.append(tuple(map(int, input().split())))
    for _ in range(m):
        checkpoints.append(tuple(map(int, input().split())))
    nearest_checkpoints = solve(students, checkpoints)
    for nearest_checkpoint in nearest_checkpoints:
        print(checkpoints.index(nearest_checkpoint) + 1)

if __name__ == '__main__':
    main()

