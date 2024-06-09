
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Initialize variables to keep track of the current group and the current position in the string
    current_group = ""
    current_position = 0
    
    # Loop through each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, start a new group
        if char == "(":
            # If the current group is not empty, add it to the list of groups
            if current_group != "":
                groups.append(current_group)
                current_group = ""
            # Add the opening parenthesis to the current group
            current_group += char
        # If the character is a closing parenthesis, add it to the current group
        elif char == ")":
            current_group += char
        # If the character is a space, ignore it
        elif char == " ":
            pass
        # If the character is not a parenthesis or a space, raise an error
        else:
            raise ValueError("Invalid character in input string")
    
    # Add the final group to the list of groups
    if current_group != "":
        groups.append(current_group)
    
    return groups

