
def get_distance(student, tutor):
    return abs(student[0] - tutor[0]) + abs(student[1] - tutor[1])

def solve(students, tutors):
    # Initialize the minimum distance as a large number
    min_distance = 1000000000
    # Iterate over all possible pairings of students and tutors
    for i in range(len(students)):
        for j in range(len(tutors)):
            # Calculate the distance between the current student and tutor
            distance = get_distance(students[i], tutors[j])
            # If the distance is less than the minimum distance, update the minimum distance
            if distance < min_distance:
                min_distance = distance
    # Return the minimum distance
    return min_distance

def main():
    # Read the number of students and tutors
    n = int(input())
    # Read the locations of the students
    students = []
    for i in range(n):
        students.append(list(map(int, input().split())))
    # Read the locations of the tutors
    tutors = []
    for i in range(n):
        tutors.append(list(map(int, input().split())))
    # Solve the problem
    result = solve(students, tutors)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

