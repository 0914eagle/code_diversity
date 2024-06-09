
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Iterate through the characters of the input string
    for char in paren_string:
        # If the current character is an opening brace, start a new group
        if char == "(":
            current_group = ""
        
        # If the current character is a closing brace, add the current group to the list of groups
        elif char == ")":
            groups.append(current_group)
        
        # If the current character is not a brace, add it to the current group
        else:
            current_group += char
    
    # Return the list of groups
    return groups

