
def get_smallest_integer(string_n, substring):
    
    # Convert the string to a list of individual digits
    string_list = [int(digit) for digit in string_n]
    
    # Convert the substring to a list of individual digits
    substring_list = [int(digit) for digit in substring]
    
    # Initialize a set to store the possible values of n
    possible_ns = set()
    
    # Iterate over the possible values of n
    for n in range(1000000):
        # Convert the current value of n to a string
        n_string = str(n)
        
        # Check if the current value of n is a permutation of the original string
        if all(digit in substring_list for digit in n_string):
            # Add the current value of n to the set of possible values
            possible_ns.add(n)
    
    # Return the smallest value of n in the set of possible values
    return min(possible_ns)

def main():
    # Read the input data from stdin
    string_n = input()
    substring = input()
    
    # Call the function to get the smallest possible initial integer n
    smallest_n = get_smallest_integer(string_n, substring)
    
    # Print the result
    print(smallest_n)

if __name__ == '__main__':
    main()

