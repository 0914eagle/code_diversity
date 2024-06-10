
def get_min_x(n, d, b, a):
    # Initialize variables
    x_1 = 0
    x_2 = 0
    visited = [False] * n
    instructor_1 = 1
    instructor_2 = n

    # Loop through each room
    for i in range(n):
        # Get the number of students in the current room
        num_students = a[i]

        # If the current room is not visited
        if not visited[i]:
            # Set the current room as visited
            visited[i] = True

            # If the number of students is not equal to b
            if num_students != b:
                # Increment the number of rooms where the first instructor will write down the number of students
                x_1 += 1

            # Move the first instructor to the next room
            instructor_1 += 1

            # If the first instructor is at the last room
            if instructor_1 == n + 1:
                # Move the first instructor to the first room
                instructor_1 = 1

            # If the number of students is not equal to b
            if num_students != b:
                # Increment the number of rooms where the second instructor will write down the number of students
                x_2 += 1

            # Move the second instructor to the previous room
            instructor_2 -= 1

            # If the second instructor is at the first room
            if instructor_2 == 0:
                # Move the second instructor to the last room
                instructor_2 = n

    # Return the minimum value of x_1 and x_2
    return min(x_1, x_2)

def main():
    # Read the input
    n, d, b = map(int, input().split())
    a = list(map(int, input().split()))

    # Call the get_min_x function and print the result
    print(get_min_x(n, d, b, a))

if __name__ == '__main__':
    main()

