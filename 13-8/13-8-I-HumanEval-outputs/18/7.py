
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Initialize an empty list to store the results
    results = []

    # Split the input string into individual groups
    groups = paren_string.split()

    # Iterate over each group
    for group in groups:
        # Initialize variables to keep track of the current level of nesting and the maximum level of nesting
        current_level = 0
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an open parenthesis, increase the current level of nesting
            if char == "(":
                current_level += 1
            # If the character is a close parenthesis, decrease the current level of nesting
            elif char == ")":
                current_level -= 1
            # If the current level of nesting is greater than the maximum level of nesting, update the maximum level of nesting
            if current_level > max_level:
                max_level = current_level

        # Add the maximum level of nesting for this group to the results list
        results.append(max_level)

    return results

