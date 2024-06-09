
def get_max_squares(num_jars, jar_contents):
    # Initialize variables
    max_squares = 0
    current_color = 1
    jar_index = 0
    jar_contents_copy = jar_contents.copy()

    # Loop through each jar and calculate the maximum number of squares that can be painted
    for i in range(num_jars):
        # Calculate the number of squares that can be painted with the current color
        num_squares = min(jar_contents_copy[current_color - 1], jar_contents_copy[current_color % num_jars])
        max_squares += num_squares

        # Update the jar contents and current color
        jar_contents_copy[current_color - 1] -= num_squares
        jar_contents_copy[current_color % num_jars] -= num_squares
        current_color += 1

    return max_squares

def main():
    num_jars = int(input())
    jar_contents = list(map(int, input().split()))
    print(get_max_squares(num_jars, jar_contents))

if __name__ == '__main__':
    main()

