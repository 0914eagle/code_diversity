
def correct_bracketing(brackets: str) -> bool:
    
    # Initialize a counter for the number of opening brackets
    opening_brackets = 0

    # Iterate through the string
    for char in brackets:
        # If the current character is an opening bracket, increment the counter
        if char == "<":
            opening_brackets += 1
        # If the current character is a closing bracket, decrement the counter
        elif char == ">":
            opening_brackets -= 1
        # If the counter goes below 0, return False
        if opening_brackets < 0:
            return False

    # If the counter is not 0 at the end of the string, return False
    if opening_brackets != 0:
        return False

    # If the counter is 0 at the end of the string, return True
    return True

