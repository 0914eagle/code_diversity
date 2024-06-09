
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separated groups
    separated_groups = []
    
    # Iterate through the input string
    for char in paren_string:
        # If the current character is an opening brace, add it to the current group
        if char == "(":
            current_group = char
        # If the current character is a closing brace, add it to the current group
        elif char == ")":
            current_group += char
            # Check if the current group is balanced (each open brace is properly closed)
            if current_group.count("(") == current_group.count(")"):
                # If the current group is balanced, add it to the list of separated groups
                separated_groups.append(current_group)
        # If the current character is a space, ignore it
        elif char.isspace():
            pass
        # If the current character is not an opening or closing brace or a space, raise a ValueError
        else:
            raise ValueError("Invalid input string")
    
    return separated_groups

