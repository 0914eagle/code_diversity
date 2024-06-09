
def correct_bracketing(brackets: str) -> bool:
    
    # Initialize a counter for the number of opening brackets
    opening_brackets = 0

    # Iterate through the string
    for bracket in brackets:
        # If the current bracket is an opening bracket, increment the counter
        if bracket == "<":
            opening_brackets += 1
        # If the current bracket is a closing bracket, decrement the counter
        elif bracket == ">":
            opening_brackets -= 1

    # If the counter is zero, then every opening bracket has a corresponding closing bracket
    return opening_brackets == 0

