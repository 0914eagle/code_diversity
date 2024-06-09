
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Initialize a list to store the results
    result = []

    # Split the input string into a list of groups
    groups = paren_string.split()

    # Iterate over the groups
    for group in groups:
        # Initialize a counter to keep track of the nesting level
        nesting_level = 0

        # Iterate over the characters in the group
        for char in group:
            # If the character is an opening parenthesis, increase the nesting level
            if char == "(":
                nesting_level += 1
            # If the character is a closing parenthesis, decrease the nesting level
            elif char == ")":
                nesting_level -= 1

        # Add the nesting level to the result list
        result.append(nesting_level)

    return result

