
def solve(students, tutors):
    # Calculate the distance between each student and tutor
    distances = []
    for student in students:
        for tutor in tutors:
            distance = abs(student[0] - tutor[0]) + abs(student[1] - tutor[1])
            distances.append((student, tutor, distance))
    
    # Sort the distances in ascending order
    distances.sort(key=lambda x: x[2])
    
    # Initialize the minimum distance traveled by the student who is worst off
    min_distance = distances[0][2]
    
    # Iterate through the distances and check if the distance traveled by the student who is worst off is less than the current distance
    for i in range(1, len(distances)):
        if distances[i][2] < min_distance:
            min_distance = distances[i][2]
        else:
            break
    
    # Return the minimum distance traveled by the student who is worst off
    return min_distance

