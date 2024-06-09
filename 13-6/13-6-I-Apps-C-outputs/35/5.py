
def get_meow_factor(string):
    # Initialize the meow factor as 0
    meow_factor = 0
    
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is 'm'
        if string[i] == 'm':
            # If it is, check if the next three characters are 'e', 'o', and 'w'
            if i + 1 < len(string) and string[i + 1] == 'e' and i + 2 < len(string) and string[i + 2] == 'o' and i + 3 < len(string) and string[i + 3] == 'w':
                # If they are, return the current meow factor
                return meow_factor
            # If the current character is 'm' and the next three characters are not 'e', 'o', and 'w', increment the meow factor by 1
            meow_factor += 1
    
    # If the string does not contain 'meow' as a substring, return -1
    return -1

def main():
    string = input("Enter a string: ")
    print(get_meow_factor(string))

if __name__ == '__main__':
    main()

