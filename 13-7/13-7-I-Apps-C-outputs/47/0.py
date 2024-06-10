
def pack_widgets(N):
    # Initialize variables
    empty_squares = 0
    widgets_packed = 0
    current_row = 0
    current_column = 0

    # Pack widgets
    while widgets_packed < N:
        # Check if the current square is empty
        if current_row % 2 == 0:
            if current_column % 2 == 0:
                empty_squares += 1
        else:
            if current_column % 2 == 1:
                empty_squares += 1

        # Move to the next square
        current_column += 1
        if current_column == 2:
            current_column = 0
            current_row += 1

        # Increment the number of widgets packed
        widgets_packed += 1

    return empty_squares

def main():
    N = int(input())
    print(pack_widgets(N))

if __name__ == '__main__':
    main()

