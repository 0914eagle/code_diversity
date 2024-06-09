
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separated groups
    separated_groups = []
    
    # Iterate through the characters of the input string
    for char in paren_string:
        # If the current character is an open parenthesis, start a new group
        if char == "(":
            current_group = char
        # If the current character is a close parenthesis, add the current group to the list of separated groups
        elif char == ")":
            separated_groups.append(current_group)
        # If the current character is a space, ignore it
        elif char == " ":
            pass
        # If the current character is not a parenthesis or a space, add it to the current group
        else:
            current_group += char
    
    return separated_groups

