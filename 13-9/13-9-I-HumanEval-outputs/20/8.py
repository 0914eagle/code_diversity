
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Iterate through the input string
    for char in paren_string:
        # If the character is an opening parenthesis, start a new group
        if char == "(":
            current_group = "("
        # If the character is a closing parenthesis, add the current group to the list of groups
        elif char == ")":
            groups.append(current_group)
        # If the character is a space, ignore it
        elif char == " ":
            continue
        # If the character is neither an opening nor closing parenthesis, add it to the current group
        else:
            current_group += char
    
    # Return the list of groups
    return groups

