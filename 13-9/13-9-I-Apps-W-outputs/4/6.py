
def get_smallest_number(display):
    # Initialize the smallest number as the initial display
    smallest_number = display
    
    # Iterate through all possible orders of pressing the buttons
    for i in range(2**len(display)):
        # Convert the binary representation of i to a list of 0s and 1s
        binary_rep = [int(x) for x in bin(i)[2:]]
        
        # Initialize the current display as the initial display
        current_display = display
        
        # Iterate through the list of 0s and 1s and apply the corresponding button press
        for j, button in enumerate(binary_rep):
            if button == 0:
                current_display = add_one(current_display)
            else:
                current_display = shift_right(current_display)
        
        # If the current display is smaller than the smallest number, update the smallest number
        if current_display < smallest_number:
            smallest_number = current_display
    
    return smallest_number

def add_one(display):
    # Add 1 to all digits in the display
    return [str((int(x) + 1) % 10) for x in display]

def shift_right(display):
    # Shift all digits in the display one position to the right
    return [display[-1]] + display[:-1]

def main():
    display = [int(x) for x in input().strip()]
    print(''.join(get_smallest_number(display)))

if __name__ == '__main__':
    main()

