
def get_smallest_integer(string, substring):
    # Convert the input string to an integer
    n = int(string)
    
    # Get the number of digits in the input string
    num_digits = len(string)
    
    # Initialize the smallest possible integer to the input string
    smallest_integer = n
    
    # Loop through all possible integers from 1 to the input string
    for i in range(1, n):
        # Get the current integer
        current_integer = i
        
        # Get the current integer as a string
        current_string = str(current_integer)
        
        # Check if the current string contains the substring
        if substring in current_string:
            # Get the number of digits in the current string
            current_num_digits = len(current_string)
            
            # Check if the current string has more digits than the input string
            if current_num_digits > num_digits:
                # Get the smallest possible integer with the given number of digits
                smallest_integer = int(current_string[:num_digits])
    
    return smallest_integer

def main():
    string, substring = input().split()
    print(get_smallest_integer(string, substring))

if __name__ == '__main__':
    main()

