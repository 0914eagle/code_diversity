
def get_max_height(n, h1, h2):
    # Initialize variables
    max_height = 0
    current_height = 0
    current_row = 1
    chosen_students = []

    # Iterate through the students in each row
    for i in range(n):
        # If the current student is not in the chosen students list, add it to the list
        if h1[i] not in chosen_students and h2[i] not in chosen_students:
            # Add the current student to the chosen students list
            chosen_students.append(h1[i])
            chosen_students.append(h2[i])
            # Update the current height
            current_height += h1[i] + h2[i]
            # Update the maximum height if necessary
            if current_height > max_height:
                max_height = current_height
            # Update the current row
            current_row = 3 - current_row
        # If the current student is already in the chosen students list, move to the next student
        else:
            continue

    # Return the maximum height
    return max_height

if __name__ == '__main__':
    n = int(input())
    h1 = list(map(int, input().split()))
    h2 = list(map(int, input().split()))
    print(get_max_height(n, h1, h2))

