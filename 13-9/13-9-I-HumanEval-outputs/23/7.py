
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Initialize an empty list to store the results
    results = []

    # Split the input string into a list of groups based on spaces
    groups = paren_string.split()

    # Iterate over each group and find the maximum level of nesting
    for group in groups:
        # Initialize variables to keep track of the current level of nesting and the maximum level
        current_level = 0
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the current level of nesting
            if char == "(":
                current_level += 1
            # If the character is a closing parenthesis, decrease the current level of nesting
            elif char == ")":
                current_level -= 1

            # Update the maximum level of nesting if necessary
            max_level = max(max_level, current_level)

        # Add the maximum level of nesting for this group to the results list
        results.append(max_level)

    return results

