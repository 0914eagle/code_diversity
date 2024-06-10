
def get_smallest_empty_squares(N):
    # Initialize variables
    smallest_empty_squares = N
    current_empty_squares = 0
    current_box_size = 1

    # Iterate through possible box sizes
    while current_box_size <= int(N ** 0.5):
        # Calculate the number of widgets that can be packed in the current box
        num_widgets = current_box_size ** 2

        # Check if the number of widgets is greater than the number of widgets to be packed
        if num_widgets > N:
            break

        # Calculate the number of empty squares in the current box
        current_empty_squares = current_box_size ** 2 - N

        # Update the smallest number of empty squares if necessary
        if current_empty_squares < smallest_empty_squares:
            smallest_empty_squares = current_empty_squares

        # Increment the box size
        current_box_size += 1

    return smallest_empty_squares

def main():
    N = int(input())
    print(get_smallest_empty_squares(N))

if __name__ == '__main__':
    main()

