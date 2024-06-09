
def get_max_height(n, h1, h2):
    # Initialize variables
    max_height = 0
    current_height = 0
    current_row = 1
    chosen_students = []

    # Iterate through the students
    for i in range(n):
        # If the current student is from the same row as the previous student, skip it
        if current_row == 1 and i in chosen_students or current_row == 2 and i not in chosen_students:
            continue
        # Add the height of the current student to the total height
        current_height += h1[i] if current_row == 1 else h2[i]
        # Add the current student to the list of chosen students
        chosen_students.append(i)
        # If the total height is greater than the maximum height, update the maximum height
        if current_height > max_height:
            max_height = current_height
        # Toggle the current row
        current_row = 2 if current_row == 1 else 1

    return max_height

if __name__ == '__main__':
    n = int(input())
    h1 = list(map(int, input().split()))
    h2 = list(map(int, input().split()))
    print(get_max_height(n, h1, h2))

