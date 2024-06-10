
def find_min_distance(student_locations, tutor_locations):
    # Calculate the distance between each student and tutor
    distances = []
    for student in student_locations:
        dist = []
        for tutor in tutor_locations:
            dist.append(abs(student[0] - tutor[0]) + abs(student[1] - tutor[1]))
        distances.append(dist)
    
    # Find the minimum distance for each student
    min_distances = []
    for dist in distances:
        min_distances.append(min(dist))
    
    # Find the maximum minimum distance
    max_min_distance = max(min_distances)
    
    # Return the maximum minimum distance
    return max_min_distance

def main():
    num_students, num_tutors = map(int, input().split())
    student_locations = []
    for _ in range(num_students):
        student_locations.append(list(map(int, input().split())))
    tutor_locations = []
    for _ in range(num_tutors):
        tutor_locations.append(list(map(int, input().split())))
    print(find_min_distance(student_locations, tutor_locations))

if __name__ == '__main__':
    main()

