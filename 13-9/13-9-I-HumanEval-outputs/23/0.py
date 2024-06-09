
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Initialize an empty list to store the results
    results = []

    # Split the input string into individual groups
    groups = paren_string.split(" ")

    # Iterate over each group
    for group in groups:
        # Initialize variables to keep track of the current depth and maximum depth
        current_depth = 0
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the depth
            if char == "(":
                current_depth += 1
            # If the character is a closing parenthesis, decrease the depth
            elif char == ")":
                current_depth -= 1
            # Update the maximum depth if the current depth is greater than the previous maximum depth
            max_depth = max(max_depth, current_depth)

        # Add the maximum depth to the results list
        results.append(max_depth)

    return results

