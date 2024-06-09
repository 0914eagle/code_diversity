
def get_max_height(n, h1, h2):
    # Initialize variables
    max_height = 0
    current_height = 0
    current_row = 1
    chosen_students = []

    # Iterate through the students
    for i in range(n):
        # Check if the current student is in the same row as the previous student
        if current_row == 1:
            # If the current student is in the same row as the previous student, skip them
            if i in chosen_students:
                continue

        # Add the height of the current student to the current height
        current_height += h1[i]

        # Check if the current height is greater than the maximum height
        if current_height > max_height:
            # If the current height is greater than the maximum height, update the maximum height
            max_height = current_height

        # Add the current student to the list of chosen students
        chosen_students.append(i)

        # Update the current row
        current_row = 2 if current_row == 1 else 1

    # Return the maximum height
    return max_height

def main():
    n = int(input())
    h1 = list(map(int, input().split()))
    h2 = list(map(int, input().split()))
    print(get_max_height(n, h1, h2))

if __name__ == '__main__':
    main()

