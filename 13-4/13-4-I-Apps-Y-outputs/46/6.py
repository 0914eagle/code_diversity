
def get_shifted_string(s, n):
    # Convert the input string to a list of characters
    char_list = list(s)
    
    # Loop through each character in the list
    for i in range(len(char_list)):
        # Calculate the new position of the character
        new_pos = (ord(char_list[i]) - ord('A') + n) % 26
        
        # Update the character at the new position
        char_list[i] = chr(ord('A') + new_pos)
    
    # Return the updated string
    return "".join(char_list)

def main():
    # Read the input from stdin
    n = int(input())
    s = input()
    
    # Call the function to get the shifted string
    shifted_string = get_shifted_string(s, n)
    
    # Print the shifted string to stdout
    print(shifted_string)

if __name__ == '__main__':
    main()

