
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Initialize an empty list to store the results
    results = []

    # Split the input string into individual groups
    groups = paren_string.split(" ")

    # Iterate over each group
    for group in groups:
        # Initialize a counter to keep track of the nesting level
        nesting_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the nesting level
            if char == "(":
                nesting_level += 1
            # If the character is a closing parenthesis, decrease the nesting level
            elif char == ")":
                nesting_level -= 1

        # Add the final nesting level to the results list
        results.append(nesting_level)

    return results

