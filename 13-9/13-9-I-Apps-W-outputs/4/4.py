
def get_smallest_number(display):
    # Initialize a variable to store the smallest number
    smallest_number = ""
    
    # Iterate through each digit in the display
    for digit in display:
        # If the digit is not zero, add it to the smallest number
        if digit != "0":
            smallest_number += digit
    
    # If the smallest number is empty, set it to "0"
    if not smallest_number:
        smallest_number = "0"
    
    return smallest_number

def get_desired_display(display):
    # Get the smallest number from the display
    smallest_number = get_smallest_number(display)
    
    # Create a list to store the digits of the smallest number
    smallest_number_list = list(smallest_number)
    
    # Iterate through each digit in the display
    for i in range(len(display)):
        # If the digit is not the smallest digit, shift it to the right
        if display[i] != smallest_number_list[i]:
            display = display[1:] + display[:1]
    
    return display

def main():
    # Read the number of digits and the initial display from stdin
    n = int(input())
    display = input()
    
    # Get the desired display
    desired_display = get_desired_display(display)
    
    # Print the desired display
    print(desired_display)

if __name__ == '__main__':
    main()

