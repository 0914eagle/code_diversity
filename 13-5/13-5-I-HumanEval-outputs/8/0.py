
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
        # If the character is a close parenthesis, add the current group to the list of groups and reset the current group
        elif char == ")":
            groups.append(current_group)
            current_group = ""
        # If the character is a space, ignore it
        elif char == " ":
            pass
        # If the character is any other character, add it to the current group
        else:
            current_group += char
    
    # Add the last group to the list of groups
    groups.append(current_group)
    
    return groups

