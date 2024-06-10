
def bjarki_editor(string):
    # Initialize an empty string to store the corrected string
    corrected_string = ""
    
    # Iterate through the input string
    for char in string:
        # If the current character is not '<', append it to the corrected string
        if char != "<":
            corrected_string += char
        # If the current character is '<' and the previous character is not '<', remove the previous character from the corrected string
        elif char == "<" and corrected_string and corrected_string[-1] != "<":
            corrected_string = corrected_string[:-1]
    
    # Return the corrected string
    return corrected_string

def main():
    # Read a single line of input from stdin and split it into a list of characters
    string = input().split()
    
    # Pass the list of characters to the bjarki_editor function and store the result in a variable
    corrected_string = bjarki_editor(string)
    
    # Print the corrected string to stdout
    print(corrected_string)

if __name__ == '__main__':
    main()

