
def get_number_of_students_to_redirect(n, d, b):
    # Calculate the maximum number of students that can be redirected
    max_students = 0
    for i in range(1, n):
        max_students += min(d + 1, n - i) * b
    return max_students

def get_min_number_of_rooms_with_different_number_of_students(n, d, b, a):
    # Initialize variables
    x_1 = 0
    x_2 = 0
    current_room = 1
    running_students = 0
    hidden_students = 0
    students_in_room = a[current_room]

    # Iterate through all rooms
    while current_room <= n:
        # Calculate the number of students that can run and hide
        runnable_students = min(d + 1, n - current_room)
        hideable_students = students_in_room - running_students

        # Redirect running students
        running_students -= runnable_students
        hidden_students += runnable_students

        # Hide students in the current room
        hidden_students += hideable_students
        students_in_room = 0

        # Update the number of rooms with different number of students
        if students_in_room != b:
            x_1 += 1
        if hidden_students != b:
            x_2 += 1

        # Move to the next room
        current_room += 1
        if current_room <= n:
            students_in_room = a[current_room]

    # Return the minimum number of rooms with different number of students
    return min(x_1, x_2)

def main():
    n, d, b = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_min_number_of_rooms_with_different_number_of_students(n, d, b, a))

if __name__ == '__main__':
    main()

