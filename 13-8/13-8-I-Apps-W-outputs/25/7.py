
def get_student_locations(n):
    locations = []
    for i in range(n):
        x, y = map(int, input().split())
        locations.append((x, y))
    return locations

def get_tutor_locations(n):
    locations = []
    for i in range(n):
        x, y = map(int, input().split())
        locations.append((x, y))
    return locations

def get_min_distance(student_locations, tutor_locations):
    min_distance = float('inf')
    for student in student_locations:
        for tutor in tutor_locations:
            distance = abs(student[0] - tutor[0]) + abs(student[1] - tutor[1])
            if distance < min_distance:
                min_distance = distance
    return min_distance

def solve(n):
    student_locations = get_student_locations(n)
    tutor_locations = get_tutor_locations(n)
    min_distance = get_min_distance(student_locations, tutor_locations)
    return min_distance

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

