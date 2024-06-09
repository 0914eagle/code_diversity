
def get_max_squares(jars):
    # Initialize variables
    max_squares = 0
    current_color = 1
    remaining_liters = [jar for jar in jars]

    # Iterate through the jars
    for i in range(len(jars)):
        # Check if there is enough paint for the current color
        if remaining_liters[current_color - 1] >= 1:
            # Subtract 1 liter of paint from the current color
            remaining_liters[current_color - 1] -= 1
            # Increment the number of squares painted
            max_squares += 1
            # Move to the next color
            current_color = (current_color % len(jars)) + 1
        else:
            # If there is no more paint of the current color, move to the next color
            current_color = (current_color % len(jars)) + 1

    return max_squares

def main():
    n = int(input())
    jars = list(map(int, input().split()))
    print(get_max_squares(jars))

if __name__ == '__main__':
    main()

