
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Loop through the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, start a new group
        if char == '(':
            group = '('
        # If the character is a closing parenthesis, add the current group to the list of groups
        elif char == ')':
            groups.append(group)
        # If the character is not a parentheses, add it to the current group
        else:
            group += char
    
    # Return the list of groups
    return groups

