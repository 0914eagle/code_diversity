
def get_display_state(n, state):
    # Initialize a list to store the display state
    display_state = list(state)
    
    # Convert the display state to an integer
    display_int = int("".join(map(str, display_state)))
    
    # Find the smallest possible number that can be obtained by pushing the buttons in some order
    smallest_number = find_smallest_number(display_int, n)
    
    # Convert the smallest number to a list of digits
    smallest_number_list = list(str(smallest_number))
    
    # Return the list of digits as the display state
    return smallest_number_list

def find_smallest_number(display_int, n):
    # Initialize a variable to store the smallest number found so far
    smallest_number = display_int
    
    # Loop through all possible combinations of adding 1 and shifting the display
    for i in range(n):
        # Add 1 to all the digits on the display
        display_int_plus_one = display_int + 1
        
        # Shift all the digits on the display one position to the right
        display_int_shifted = display_int_plus_one // 10
        
        # Find the smallest number that can be obtained by pushing the buttons in some order
        smallest_number = min(smallest_number, display_int_shifted)
    
    # Return the smallest number found
    return smallest_number

if __name__ == '__main__':
    n = int(input())
    state = list(map(int, input()))
    print(*get_display_state(n, state))

