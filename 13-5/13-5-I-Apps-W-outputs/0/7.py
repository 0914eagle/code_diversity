
def get_max_squares(num_jars, jar_contents):
    # Initialize variables
    max_squares = 0
    current_color = 1
    remaining_liters = [jar_contents[i] for i in range(num_jars)]

    # Iterate through the jars and calculate the maximum number of squares that can be painted
    for i in range(num_jars):
        # Calculate the number of squares that can be painted with the current color
        num_squares = min(remaining_liters[current_color - 1], remaining_liters[current_color % num_jars])

        # Update the maximum number of squares
        max_squares = max(max_squares, num_squares)

        # Update the remaining liters and the current color
        remaining_liters[current_color - 1] -= num_squares
        current_color = (current_color + 1) % num_jars

    return max_squares

def main():
    num_jars = int(input())
    jar_contents = list(map(int, input().split()))
    print(get_max_squares(num_jars, jar_contents))

if __name__ == '__main__':
    main()

