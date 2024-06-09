
def solve(a, b, c, order):
    # Convert the input strings to integers
    a = int(a)
    b = int(b)
    c = int(c)
    
    # Create a dictionary to map the characters to the integers
    char_to_int = {"A": a, "B": b, "C": c}
    
    # Create a list to store the integers in the desired order
    result = []
    
    # Iterate through the characters in the order string
    for char in order:
        # Add the integer corresponding to the character to the result list
        result.append(char_to_int[char])
    
    # Return the result list as a string, separated by spaces
    return " ".join(str(x) for x in result)

