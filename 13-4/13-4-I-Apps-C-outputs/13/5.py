
def get_meow_factor(string):
    # Initialize the meow factor to 0
    meow_factor = 0
    
    # Loop through each character in the string
    for i in range(len(string)):
        # If the current character is 'm', check if the next three characters are 'e', 'o', and 'w'
        if string[i] == 'm':
            if i + 1 < len(string) and string[i + 1] == 'e' and i + 2 < len(string) and string[i + 2] == 'o' and i + 3 < len(string) and string[i + 3] == 'w':
                # If the next three characters are 'e', 'o', and 'w', increment the meow factor by 1
                meow_factor += 1
    
    # Return the meow factor
    return meow_factor

def main():
    # Read a single line of input from stdin and convert it to a string
    string = input().strip()
    
    # Print the meow factor of the string
    print(get_meow_factor(string))

if __name__ == '__main__':
    main()

