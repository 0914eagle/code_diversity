
def get_distance(student, tutor):
    return abs(student[0] - tutor[0]) + abs(student[1] - tutor[1])

def solve(students, tutors):
    # Calculate the distance between each student and each tutor
    distances = [[get_distance(student, tutor) for tutor in tutors] for student in students]
    
    # Find the minimum distance between a student and a tutor
    min_dist = min(min(distances, key=min))
    
    # Return the minimum distance + 1
    return min_dist + 1

def main():
    num_students = int(input())
    students = []
    for _ in range(num_students):
        students.append(list(map(int, input().split())))
    
    num_tutors = int(input())
    tutors = []
    for _ in range(num_tutors):
        tutors.append(list(map(int, input().split())))
    
    print(solve(students, tutors))

if __name__ == '__main__':
    main()

