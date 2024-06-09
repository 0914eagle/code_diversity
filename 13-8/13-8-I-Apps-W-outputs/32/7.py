
def solve(n):
    # Initialize an empty string
    string = ""
    
    # Loop through each character in the string
    for i in range(n):
        # If the character is 'a', add it to the string
        if i % 2 == 0:
            string += "a"
        # If the character is 'b', add it to the string
        elif i % 3 == 0:
            string += "b"
        # If the character is 'c', add it to the string
        else:
            string += "c"
    
    # Return the string
    return string

