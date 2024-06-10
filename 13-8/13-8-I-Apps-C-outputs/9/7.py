
def get_meow_factor(string):
    # Initialize the meow factor as 0
    meow_factor = 0
    
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is 'm'
        if string[i] == 'm':
            # If it is, check if the next three characters are 'e', 'o', and 'w'
            if i < len(string) - 3 and string[i+1] == 'e' and string[i+2] == 'o' and string[i+3] == 'w':
                # If they are, return the meow factor as 1
                return 1
    
    # If the loop completes and no 'meow' substring is found, return the meow factor as 0
    return 0

def main():
    # Read a line of input from stdin and convert it to an integer
    string = input().strip()
    
    # Call the get_meow_factor function and print the result
    print(get_meow_factor(string))

if __name__ == '__main__':
    main()

