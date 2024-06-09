
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Initialize a list to store the depth of nesting for each group
    depth_list = []

    # Split the input string into a list of groups
    groups = paren_string.split()

    # Iterate over each group
    for group in groups:
        # Initialize the depth of nesting for this group to 0
        depth = 0

        # Iterate over the characters in the group
        for char in group:
            # If the character is an open parenthesis, increment the depth
            if char == "(":
                depth += 1
            # If the character is a close parenthesis, decrement the depth
            elif char == ")":
                depth -= 1

        # Add the depth of nesting for this group to the list
        depth_list.append(depth)

    return depth_list

