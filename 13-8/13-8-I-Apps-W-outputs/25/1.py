
def get_student_tutor_pairs(students, tutors):
    # Initialize a dictionary to store the pairs of students and tutors
    pairs = {}
    
    # Iterate through the students and find the tutor with the shortest distance
    for student in students:
        # Find the tutor with the shortest distance to the student
        shortest_distance = float('inf')
        for tutor in tutors:
            distance = get_distance(student, tutor)
            if distance < shortest_distance:
                shortest_distance = distance
                pairs[student] = tutor
    
    return pairs

def get_distance(point1, point2):
    # Calculate the absolute difference between the x and y coordinates of the two points
    x_diff = abs(point1[0] - point2[0])
    y_diff = abs(point1[1] - point2[1])
    
    # Return the sum of the absolute differences
    return x_diff + y_diff

def main():
    # Read the number of students and tutors
    n = int(input())
    
    # Read the locations of the students
    students = []
    for i in range(n):
        x, y = map(int, input().split())
        students.append((x, y))
    
    # Read the locations of the tutors
    tutors = []
    for i in range(n):
        x, y = map(int, input().split())
        tutors.append((x, y))
    
    # Find the optimal pairing of students to tutors
    pairs = get_student_tutor_pairs(students, tutors)
    
    # Calculate the maximum distance between any two students in a pair
    max_distance = 0
    for student, tutor in pairs.items():
        distance = get_distance(student, tutor)
        if distance > max_distance:
            max_distance = distance
    
    # Print the result
    print(max_distance)

if __name__ == '__main__':
    main()

