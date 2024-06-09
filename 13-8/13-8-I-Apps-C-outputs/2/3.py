
def solve(n, d, b, a):
    # Calculate the total number of students
    total_students = sum(a)

    # Initialize the number of rooms with different number of students
    x = 0

    # Iterate through each room
    for i in range(n):
        # Calculate the number of students in the current room
        current_room_students = a[i]

        # Calculate the number of students that can run away from the current room
        run_away_students = min(d, total_students - current_room_students)

        # Calculate the number of students that can hide in the current room
        hide_students = current_room_students - run_away_students

        # Check if the number of students in the current room is different from the official number of students
        if current_room_students != b:
            x += 1

        # Update the total number of students
        total_students -= run_away_students

    # Return the minimum possible value of the maximum of x_i
    return x

