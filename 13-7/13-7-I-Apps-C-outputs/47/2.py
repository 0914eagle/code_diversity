
def get_number_of_empty_squares(N):
    # Find the closest box size that can fit all the widgets
    box_width = int(N ** 0.5)
    box_height = int(N / box_width)

    # Calculate the number of empty squares
    empty_squares = (box_width - N) * (box_height - 1)

    return empty_squares

def main():
    N = int(input())
    print(get_number_of_empty_squares(N))

if __name__ == '__main__':
    main()

