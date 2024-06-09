
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Initialize an empty list to store the results
    results = []

    # Split the input string into a list of groups
    groups = paren_string.split()

    # Iterate over the groups
    for group in groups:
        # Initialize a counter to keep track of the level of nesting
        level = 0

        # Iterate over the characters in the group
        for char in group:
            # If the character is an opening parenthesis, increase the level of nesting
            if char == "(":
                level += 1
            # If the character is a closing parenthesis, decrease the level of nesting
            elif char == ")":
                level -= 1

        # Add the level of nesting for this group to the results list
        results.append(level)

    return results

