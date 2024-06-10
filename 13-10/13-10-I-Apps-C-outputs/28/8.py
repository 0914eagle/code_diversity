
def get_optimal_strategy(n, d, b, a):
    # Initialize the number of rooms where the first instructor will write down the number of students
    x_1 = 0
    # Initialize the number of rooms where the second instructor will write down the number of students
    x_2 = 0
    # Initialize the number of students in each room
    students = [0] * (n + 1)
    # Initialize the number of hidden students in each room
    hidden_students = [0] * (n + 1)
    # Initialize the running distance of each student
    running_distance = [0] * (n + 1)
    # Initialize the hiding status of each student
    hiding = [False] * (n + 1)

    # Populate the number of students in each room
    for i in range(1, n + 1):
        students[i] = a[i - 1]

    # Loop through each room
    for i in range(1, n + 1):
        # If the number of students in the current room is not equal to the official number of students, write down the room number
        if students[i] != b:
            if i == 1:
                x_1 += 1
            else:
                x_2 += 1

        # Loop through each student in the current room
        for j in range(1, students[i] + 1):
            # If the student is not hiding, check if they can run to another room
            if not hiding[i]:
                # Calculate the running distance of the student
                running_distance[j] = min(d, i - 1)
                # If the running distance is not zero, set the hiding status of the student to True
                if running_distance[j] != 0:
                    hiding[i] = True

    # Return the minimal possible value of the maximum of x_i
    return min(x_1, x_2)

def main():
    n, d, b = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_optimal_strategy(n, d, b, a))

if __name__ == '__main__':
    main()

