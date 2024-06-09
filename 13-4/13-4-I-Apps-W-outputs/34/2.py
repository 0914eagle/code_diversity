
def solve(students, tutors):
    # Calculate the distance between each student and tutor
    distances = []
    for student in students:
        for tutor in tutors:
            distance = abs(student[0] - tutor[0]) + abs(student[1] - tutor[1])
            distances.append((student, tutor, distance))
    
    # Sort the distances in ascending order
    distances.sort(key=lambda x: x[2])
    
    # Initialize the minimum distance traveled by the worst off student as infinity
    min_distance = float('inf')
    
    # Iterate through the sorted distances and find the minimum distance traveled by the worst off student
    for i in range(len(distances)):
        student, tutor, distance = distances[i]
        if distance > min_distance:
            break
        min_distance = distance
    
    # Return the minimum distance traveled by the worst off student as the solution
    return min_distance

