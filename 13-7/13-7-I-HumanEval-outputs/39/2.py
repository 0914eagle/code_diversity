
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Iterate through the characters of the input string
    for char in paren_string:
        # If the current character is an opening bracket, start a new group
        if char == "(":
            groups.append(char)
        # If the current character is a closing bracket, add it to the current group
        elif char == ")":
            groups[-1] += char
        # If the current character is a space, ignore it
        elif char == " ":
            pass
        # If the current character is not a bracket or space, raise an error
        else:
            raise ValueError("Invalid input string")
    
    # Return the list of separate groups
    return groups

