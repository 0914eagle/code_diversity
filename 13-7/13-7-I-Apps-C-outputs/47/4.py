
def get_min_empty_squares(N):
    # Initialize variables
    min_empty_squares = N
    W = 1
    H = 1

    # Loop through all possible box sizes
    while W <= 2 * H:
        # Calculate the number of empty squares in the current box
        empty_squares = (W - N) * (H - N)

        # Update the minimum number of empty squares
        if empty_squares < min_empty_squares:
            min_empty_squares = empty_squares

        # Increment the box size
        H += 1

    return min_empty_squares

def main():
    # Read the input
    N = int(input())

    # Call the function to get the minimum number of empty squares
    min_empty_squares = get_min_empty_squares(N)

    # Print the output
    print(min_empty_squares)

if __name__ == '__main__':
    main()

