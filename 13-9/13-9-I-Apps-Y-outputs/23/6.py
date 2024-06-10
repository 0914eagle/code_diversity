
import math
import sys

def get_manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def get_nearest_checkpoint(student, checkpoints):
    nearest_distance = math.inf
    nearest_checkpoint = -1
    for checkpoint in checkpoints:
        distance = get_manhattan_distance(student, checkpoint)
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_checkpoint = checkpoint
    return nearest_checkpoint

def main():
    n, m = map(int, input().split())
    students = []
    for _ in range(n):
        students.append(tuple(map(int, input().split())))
    checkpoints = []
    for _ in range(m):
        checkpoints.append(tuple(map(int, input().split())))
    for student in students:
        nearest_checkpoint = get_nearest_checkpoint(student, checkpoints)
        print(nearest_checkpoint)

if __name__ == '__main__':
    main()

