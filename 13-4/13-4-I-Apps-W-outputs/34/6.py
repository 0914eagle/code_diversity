
def solve(students, tutors):
    # Calculate the distance between each student and tutor
    distances = []
    for student in students:
        for tutor in tutors:
            distances.append(abs(student[0] - tutor[0]) + abs(student[1] - tutor[1]))
    
    # Sort the distances in ascending order
    distances.sort()
    
    # Return the maximum distance
    return distances[-1]

