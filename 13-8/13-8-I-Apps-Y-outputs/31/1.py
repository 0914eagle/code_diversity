
def parse_input(input_string):
    # Initialize an empty string to store the parsed input
    parsed_string = ""
    
    # Iterate through the input string
    for char in input_string:
        # If the current character is not '<', append it to the parsed string
        if char != "<":
            parsed_string += char
    
    # Return the parsed string
    return parsed_string

def main():
    # Read a single line of input from stdin and remove the trailing newline
    input_string = input().rstrip()
    
    # Call the parse_input function and store the result in a variable
    parsed_string = parse_input(input_string)
    
    # Print the parsed string to stdout
    print(parsed_string)

if __name__ == '__main__':
    main()

