
def get_smallest_number(display):
    # Initialize a list to store the digits of the smallest number
    smallest_num = [0] * len(display)

    # Iterate through each digit of the display
    for i in range(len(display)):
        # If the current digit is not the smallest, update the smallest number
        if display[i] != smallest_num[i]:
            smallest_num[i] = display[i]

    # Return the smallest number
    return smallest_num

def get_next_number(display):
    # Initialize a list to store the next number
    next_num = [0] * len(display)

    # Iterate through each digit of the display
    for i in range(len(display)):
        # If the current digit is 9, set it to 0
        if display[i] == 9:
            next_num[i] = 0
        # Otherwise, increment the digit
        else:
            next_num[i] = display[i] + 1

    # Return the next number
    return next_num

def get_next_display(display):
    # Get the next number
    next_num = get_next_number(display)

    # Get the smallest number
    smallest_num = get_smallest_number(next_num)

    # Return the smallest number
    return smallest_num

def main():
    # Read the number of digits and the initial state of the display
    n = int(input())
    display = list(map(int, input()))

    # Print the desired state of the display
    print(*get_next_display(display), sep='')

if __name__ == '__main__':
    main()

