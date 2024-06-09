
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separated groups
    separated_groups = []
    
    # Iterate through the input string
    for char in paren_string:
        # If the current character is an open parenthesis, start a new group
        if char == "(":
            current_group = ""
        
        # If the current character is a close parenthesis, end the current group
        elif char == ")":
            separated_groups.append(current_group)
            current_group = ""
        
        # If the current character is not a parenthesis, append it to the current group
        else:
            current_group += char
    
    return separated_groups

