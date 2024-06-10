
def get_smallest_number(display):
    # Convert the display to a list of integers
    display = [int(x) for x in display]
    
    # Find the smallest number that can be obtained by pushing the buttons in some order
    smallest_number = min(get_all_possible_numbers(display))
    
    # Return the smallest number as a string
    return "".join(str(x) for x in smallest_number)

def get_all_possible_numbers(display):
    # Create a list to store all possible numbers
    all_possible_numbers = []
    
    # Add the initial number to the list
    all_possible_numbers.append(display)
    
    # Loop until the smallest number is found
    while True:
        # Get the current number
        current_number = all_possible_numbers[-1]
        
        # Add 1 to all digits
        new_number = [x+1 for x in current_number]
        
        # Add the new number to the list
        all_possible_numbers.append(new_number)
        
        # Shift all digits one position to the right
        new_number = new_number[1:] + [new_number[0]]
        
        # Add the new number to the list
        all_possible_numbers.append(new_number)
        
        # If the smallest number is found, return the list of all possible numbers
        if new_number == sorted(all_possible_numbers)[0]:
            return all_possible_numbers

def main():
    # Read the input
    n = int(input())
    display = input()
    
    # Print the output
    print(get_smallest_number(display))

if __name__ == '__main__':
    main()

