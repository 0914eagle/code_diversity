
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups: List[str] = []
    
    # Initialize variables to keep track of the current group and the current level of nesting
    current_group: str = ""
    nesting_level: int = 0
    
    # Iterate through the characters of the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increase the nesting level
        if char == "(":
            nesting_level += 1
        # If the character is a closing parenthesis, decrease the nesting level
        elif char == ")":
            nesting_level -= 1
        # If the character is not a parenthesis, add it to the current group
        else:
            current_group += char
        
        # If the nesting level is 0, we have reached the end of a group, so add the current group to the list of groups and start a new group
        if nesting_level == 0:
            groups.append(current_group)
            current_group = ""
    
    # Return the list of groups
    return groups

