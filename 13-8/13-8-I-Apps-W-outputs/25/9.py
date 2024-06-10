
import math

def get_distance(student, tutor):
    return abs(student[0] - tutor[0]) + abs(student[1] - tutor[1])

def get_min_distance_pair(students, tutors):
    min_distance = math.inf
    min_pair = None
    for student in students:
        for tutor in tutors:
            distance = get_distance(student, tutor)
            if distance < min_distance:
                min_distance = distance
                min_pair = (student, tutor)
    return min_pair

def solve(students, tutors):
    min_distance = math.inf
    min_pair = None
    for student in students:
        for tutor in tutors:
            distance = get_distance(student, tutor)
            if distance < min_distance:
                min_distance = distance
                min_pair = (student, tutor)
    return min_distance

def main():
    n = int(input())
    students = []
    for i in range(n):
        students.append(tuple(map(int, input().split())))
    tutors = []
    for i in range(n):
        tutors.append(tuple(map(int, input().split())))
    print(solve(students, tutors))

if __name__ == '__main__':
    main()

