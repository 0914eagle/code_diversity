
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Loop through each character in the input string
    for char in paren_string:
        # If the character is an opening brace, append it to the current group
        if char == "(":
            current_group = "("
        # If the character is a closing brace, append it to the current group and add the group to the list
        elif char == ")":
            current_group += ")"
            groups.append(current_group)
        # If the character is a space, ignore it
        elif char == " ":
            pass
    
    return groups

