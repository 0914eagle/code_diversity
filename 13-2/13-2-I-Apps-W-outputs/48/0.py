
def get_max_height(n, h1, h2):
    # Initialize variables
    max_height = 0
    current_height = 0
    current_row = 1
    chosen_students = []

    # Iterate through the students
    for i in range(n):
        # Check if the current student is from the same row as the previous chosen student
        if current_row == 1:
            # If the current student is from the same row, skip them
            if i in chosen_students:
                continue
        # Add the current student to the chosen students list
        chosen_students.append(i)
        # Update the current height
        current_height += h1[i]
        # Update the current row
        current_row = 3 - current_row

    # Return the maximum height
    return current_height

def main():
    # Read the input
    n = int(input())
    h1 = list(map(int, input().split()))
    h2 = list(map(int, input().split()))

    # Call the function to get the maximum height
    max_height = get_max_height(n, h1, h2)

    # Print the result
    print(max_height)

if __name__ == '__main__':
    main()

