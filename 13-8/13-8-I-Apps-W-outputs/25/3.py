
def get_pairing(students, tutors):
    # Initialize the distance matrix with 0s
    distance_matrix = [[0 for _ in range(len(tutors))] for _ in range(len(students))]

    # Fill in the distance matrix with the appropriate distances
    for i in range(len(students)):
        for j in range(len(tutors)):
            distance_matrix[i][j] = abs(students[i][0] - tutors[j][0]) + abs(students[i][1] - tutors[j][1])

    # Create a dictionary to map each student to their tutor with the minimum distance
    student_tutor_map = {}
    for i in range(len(students)):
        student_tutor_map[i] = min(range(len(tutors)), key=lambda x: distance_matrix[i][x])

    # Create a dictionary to map each tutor to their student with the minimum distance
    tutor_student_map = {}
    for j in range(len(tutors)):
        tutor_student_map[j] = min(range(len(students)), key=lambda x: distance_matrix[x][j])

    # Check if the pairing is valid
    for i in range(len(students)):
        for j in range(len(tutors)):
            if distance_matrix[student_tutor_map[i]][j] > j:
                return -1

    # If the pairing is valid, return the maximum distance between any two students
    return max(max(distance_matrix[i][student_tutor_map[i]] for i in range(len(students))), max(distance_matrix[tutor_student_map[j]][j] for j in range(len(tutors))))

def main():
    num_students, num_tutors = map(int, input().split())
    students = [tuple(map(int, input().split())) for _ in range(num_students)]
    tutors = [tuple(map(int, input().split())) for _ in range(num_tutors)]
    print(get_pairing(students, tutors))

if __name__ == '__main__':
    main()

