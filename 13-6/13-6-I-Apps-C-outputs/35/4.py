
def get_meow_factor(string):
    # Initialize the meow factor to 0
    meow_factor = 0
    
    # Loop through each character in the string
    for i in range(len(string)):
        # If the current character is 'm', check if the next three characters are 'e', 'o', and 'w'
        if string[i] == 'm':
            if i + 1 < len(string) and string[i + 1] == 'e' and i + 2 < len(string) and string[i + 2] == 'o' and i + 3 < len(string) and string[i + 3] == 'w':
                # If they are, return the meow factor
                return meow_factor
            # If they are not, increment the meow factor
            meow_factor += 1
    
    # If the string does not contain 'meow' as a substring, return -1
    return -1

def main():
    # Read a string from stdin
    string = input()
    
    # Call the get_meow_factor function and print the result
    print(get_meow_factor(string))

if __name__ == '__main__':
    main()

