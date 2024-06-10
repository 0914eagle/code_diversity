
def get_smallest_number(n, display):
    # Initialize the smallest number as the initial display
    smallest_number = display
    
    # Loop through all possible numbers
    for i in range(10**n):
        # Convert the current number to a string
        current_number = str(i)
        
        # Pad the current number with leading zeros
        current_number = current_number.zfill(n)
        
        # Check if the current number is smaller than the smallest number
        if current_number < smallest_number:
            # Update the smallest number
            smallest_number = current_number
    
    # Return the smallest number
    return smallest_number

def main():
    # Read the number of digits and the initial state of the display
    n = int(input())
    display = input()
    
    # Get the smallest number
    smallest_number = get_smallest_number(n, display)
    
    # Print the smallest number
    print(smallest_number)

if __name__ == '__main__':
    main()

