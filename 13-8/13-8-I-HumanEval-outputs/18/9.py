
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Initialize an empty list to store the results
    results = []

    # Split the input string into individual groups
    groups = paren_string.split()

    # Iterate over each group
    for group in groups:
        # Initialize the current depth of nesting to 0
        depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the depth
            if char == "(":
                depth += 1
            # If the character is a closing parenthesis, decrease the depth
            elif char == ")":
                depth -= 1

        # Add the final depth to the results list
        results.append(depth)

    return results

