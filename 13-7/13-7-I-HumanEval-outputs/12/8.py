
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Initialize an empty list to store the results
    result = []

    # Split the input string into individual groups
    groups = paren_string.split()

    # Iterate over each group
    for group in groups:
        # Initialize variables to keep track of the current depth and maximum depth
        depth, max_depth = 0, 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the depth
            if char == "(":
                depth += 1
            # If the character is a closing parenthesis, decrease the depth
            elif char == ")":
                depth -= 1
            # Update the maximum depth if the current depth is greater than the previous maximum depth
            max_depth = max(max_depth, depth)

        # Add the maximum depth for the current group to the result list
        result.append(max_depth)

    return result

