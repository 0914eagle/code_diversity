
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

def get_pairing(students, tutors):
    distances = []
    for student in students:
        for tutor in tutors:
            distances.append(get_distance(student, tutor))
    return min(distances)

def solve(N, students, tutors):
    min_distance = get_pairing(students, tutors)
    for i in range(N):
        student = students[i]
        for j in range(N):
            tutor = tutors[j]
            if get_distance(student, tutor) > min_distance:
                continue
            students_copy = students[:]
            tutors_copy = tutors[:]
            students_copy.pop(i)
            tutors_copy.pop(j)
            min_distance_copy = get_pairing(students_copy, tutors_copy)
            if min_distance_copy < min_distance:
                min_distance = min_distance_copy
                break
    return min_distance

if __name__ == '__main__':
    N, students, tutors = read_input()
    print(solve(N, students, tutors))

