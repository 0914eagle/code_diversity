
def get_meow_factor(string):
    # Initialize a variable to store the meow factor
    meow_factor = 0
    
    # Loop through each character in the string
    for i in range(len(string)):
        # If the current character is 'm', check if the next three characters are 'e', 'o', and 'w'
        if string[i] == 'm':
            if string[i+1:i+4] == 'eow':
                # If they are, increase the meow factor by 1
                meow_factor += 1
    
    # Return the meow factor
    return meow_factor

def main():
    # Take input from the user
    string = input("Enter a string: ")
    
    # Call the get_meow_factor function and print the result
    print(get_meow_factor(string))

if __name__ == '__main__':
    main()

