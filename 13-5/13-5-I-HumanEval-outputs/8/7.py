
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Iterate through the characters of the input string
    for char in paren_string:
        # If the current character is an opening brace, append it to the current group
        if char == "(":
            current_group = char
        # If the current character is a closing brace, append it to the current group
        elif char == ")":
            current_group += char
            # If the current group is balanced (i.e., each open brace is properly closed), append it to the list of groups
            if is_balanced(current_group):
                groups.append(current_group)
        # If the current character is a space, ignore it
        elif char == " ":
            pass
        # If the current character is not a brace or a space, raise a ValueError
        else:
            raise ValueError("Invalid input string")
    
    return groups

def is_balanced(group: str) -> bool:
    
    # Initialize a counter to keep track of the number of opening and closing braces
    count = 0
    
    # Iterate through the characters of the group
    for char in group:
        # If the current character is an opening brace, increment the counter
        if char == "(":
            count += 1
        # If the current character is a closing brace, decrement the counter
        elif char == ")":
            count -= 1
    
    # If the counter is zero, the group is balanced
    return count == 0

