
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Initialize a list to store the deepest level of nesting for each group
    nesting_levels = []

    # Split the input string into individual groups
    groups = paren_string.split()

    # Iterate over each group
    for group in groups:
        # Initialize a counter to keep track of the current level of nesting
        current_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the level of nesting
            if char == "(":
                current_level += 1
            # If the character is a closing parenthesis, decrease the level of nesting
            elif char == ")":
                current_level -= 1

        # Add the deepest level of nesting for this group to the list
        nesting_levels.append(current_level)

    return nesting_levels

