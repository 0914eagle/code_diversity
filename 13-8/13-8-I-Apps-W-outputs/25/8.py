
def read_input():
    N = int(input())
    students = []
    for _ in range(N):
        students.append(tuple(map(int, input().split())))
    tutors = []
    for _ in range(N):
        tutors.append(tuple(map(int, input().split())))
    return N, students, tutors

def get_distance(student, tutor):
    return abs(student[0] - tutor[0]) + abs(student[1] - tutor[1])

def get_min_distance(student, tutors):
    return min(get_distance(student, tutor) for tutor in tutors)

def solve(N, students, tutors):
    min_dist = 10 ** 10
    for student in students:
        dist = get_min_distance(student, tutors)
        if dist < min_dist:
            min_dist = dist
    return min_dist

def main():
    N, students, tutors = read_input()
    print(solve(N, students, tutors))

if __name__ == '__main__':
    main()

