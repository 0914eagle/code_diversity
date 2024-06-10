
def get_meow_factor(string):
    # Initialize the meow factor to 0
    meow_factor = 0
    
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is 'm'
        if string[i] == 'm':
            # If it is, check if the next three characters are 'e', 'o', and 'w'
            if i + 1 < len(string) and string[i + 1] == 'e' and i + 2 < len(string) and string[i + 2] == 'o' and i + 3 < len(string) and string[i + 3] == 'w':
                # If they are, return the meow factor
                return meow_factor
            # If the current character is 'm' and the next three characters are not 'e', 'o', and 'w', increment the meow factor
            else:
                meow_factor += 1
    
    # If the string does not contain the word "meow", return -1
    return -1

def main():
    # Read a single line of input from stdin and save it to our variable, string
    string = input()
    
    # Call our get_meow_factor function and save its result to our variable, meow_factor
    meow_factor = get_meow_factor(string)
    
    # Print the meow factor
    print(meow_factor)

if __name__ == '__main__':
    main()

