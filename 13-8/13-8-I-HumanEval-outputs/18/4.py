
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Initialize an empty list to store the depth of nesting for each group
    depth_list = []

    # Split the input string into individual groups
    groups = paren_string.split()

    # Iterate over each group
    for group in groups:
        # Initialize depth variable to 0
        depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the depth
            if char == '(':
                depth += 1
            # If the character is a closing parenthesis, decrease the depth
            elif char == ')':
                depth -= 1

        # Add the depth to the depth list
        depth_list.append(depth)

    return depth_list

