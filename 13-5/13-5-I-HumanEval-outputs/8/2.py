
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Initialize variables to keep track of the current group and the current position in the string
    current_group = ""
    current_position = 0
    
    # Loop through each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, start a new group
        if char == "(":
            current_group = "("
        # If the character is a close parenthesis, end the current group
        elif char == ")":
            current_group += ")"
            groups.append(current_group)
            current_group = ""
        # If the character is a space, ignore it
        elif char == " ":
            pass
        # If the character is anything else, add it to the current group
        else:
            current_group += char
    
    # Return the list of separate groups
    return groups

