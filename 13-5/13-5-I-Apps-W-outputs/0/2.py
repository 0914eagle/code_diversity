
def get_max_squares(num_jars, jar_sizes):
    # Initialize variables
    max_squares = 0
    current_color = 1
    current_square = 1

    # Loop through each jar and calculate the maximum number of squares that can be painted
    for i in range(num_jars):
        # Calculate the number of squares that can be painted with the current color
        num_squares = min(jar_sizes[i], current_square)

        # Update the maximum number of squares
        max_squares += num_squares

        # Update the current color and current square
        current_color = (current_color + 1) % (num_jars + 1)
        current_square -= num_squares

    return max_squares

def main():
    num_jars = int(input())
    jar_sizes = list(map(int, input().split()))
    print(get_max_squares(num_jars, jar_sizes))

if __name__ == '__main__':
    main()

