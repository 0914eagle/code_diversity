
def find_smallest_number(n, display):
    # Initialize the smallest number as the initial display
    smallest_number = display
    
    # Loop through all possible combinations of buttons
    for i in range(2**n):
        # Convert the binary representation of i to a list of 0s and 1s
        binary_rep = [int(x) for x in bin(i)[2:]]
        
        # Initialize the current display as the initial display
        current_display = display
        
        # Loop through the binary representation and apply the appropriate button presses
        for j in range(n):
            if binary_rep[j] == 0:
                current_display = add_one(current_display)
            else:
                current_display = shift_right(current_display)
        
        # If the current display is smaller than the smallest number, update the smallest number
        if current_display < smallest_number:
            smallest_number = current_display
    
    return smallest_number

def add_one(display):
    return [str((int(x) + 1) % 10) for x in display]

def shift_right(display):
    return [display[-1] + display[:-1]]

if __name__ == '__main__':
    n = int(input())
    display = list(input())
    print(''.join(find_smallest_number(n, display)))

