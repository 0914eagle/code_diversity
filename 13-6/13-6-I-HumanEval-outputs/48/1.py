
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Loop through each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, start a new group
        if char == "(":
            group = "("
        # If the character is a close parenthesis, add the group to the list and reset the group variable
        elif char == ")":
            groups.append(group)
            group = ""
    
    # Return the list of separate groups
    return groups

