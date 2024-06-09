
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Loop through each character in the input string
    for char in paren_string:
        # If the character is an opening brace, append it to the current group
        if char == "(":
            groups.append(char)
        # If the character is a closing brace, append it to the current group
        elif char == ")":
            groups[-1] += char
        # If the character is a space, ignore it
        elif char == " ":
            pass
        # If the character is neither an opening nor closing brace, raise an error
        else:
            raise ValueError("Invalid character in input string")
    
    # Return the list of separate groups
    return groups

