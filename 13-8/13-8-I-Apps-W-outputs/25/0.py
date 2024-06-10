
def get_student_locations(num_students):
    locations = []
    for _ in range(num_students):
        x, y = map(int, input().split())
        locations.append((x, y))
    return locations

def get_tutor_locations(num_tutors):
    locations = []
    for _ in range(num_tutors):
        x, y = map(int, input().split())
        locations.append((x, y))
    return locations

def get_pairing_distance(student, tutor):
    return abs(student[0] - tutor[0]) + abs(student[1] - tutor[1])

def get_min_pairing_distance(student_locations, tutor_locations):
    min_distance = float('inf')
    for student in student_locations:
        for tutor in tutor_locations:
            distance = get_pairing_distance(student, tutor)
            if distance < min_distance:
                min_distance = distance
    return min_distance

def get_max_pairing_distance(student_locations, tutor_locations):
    max_distance = 0
    for student in student_locations:
        for tutor in tutor_locations:
            distance = get_pairing_distance(student, tutor)
            if distance > max_distance:
                max_distance = distance
    return max_distance

def get_optimal_pairing_distance(student_locations, tutor_locations):
    min_distance = get_min_pairing_distance(student_locations, tutor_locations)
    max_distance = get_max_pairing_distance(student_locations, tutor_locations)
    return min(min_distance, max_distance)

def main():
    num_students = int(input())
    student_locations = get_student_locations(num_students)
    num_tutors = int(input())
    tutor_locations = get_tutor_locations(num_tutors)
    print(get_optimal_pairing_distance(student_locations, tutor_locations))

if __name__ == '__main__':
    main()

