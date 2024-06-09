
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Iterate through the characters of the input string
    for char in paren_string:
        # If the current character is an opening bracket, append it to the current group
        if char == "(":
            current_group = char
        # If the current character is a closing bracket, append it to the current group
        elif char == ")":
            current_group += char
            # Add the current group to the list of groups
            groups.append(current_group)
        # If the current character is a space, ignore it
        elif char == " ":
            pass
        # If the current character is not a bracket or a space, raise a ValueError
        else:
            raise ValueError("Invalid character in input string")
    
    # Return the list of groups
    return groups

