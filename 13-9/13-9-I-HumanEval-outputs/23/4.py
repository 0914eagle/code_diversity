
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Initialize an empty list to store the depths of nesting
    depths = []

    # Split the input string into individual groups
    groups = paren_string.split()

    # Loop through each group
    for group in groups:
        # Initialize the current depth to 0
        current_depth = 0

        # Loop through each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the depth
            if char == "(":
                current_depth += 1
            # If the character is a closing parenthesis, decrease the depth
            elif char == ")":
                current_depth -= 1

        # Add the final depth to the list of depths
        depths.append(current_depth)

    return depths

