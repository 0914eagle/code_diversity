
from typing import List

def match_parens(lst: List[str]) -> str:
    
    # Initialize a counter for open and close parentheses
    open_count = 0
    close_count = 0

    # Iterate through the list of strings
    for string in lst:
        # Iterate through the characters in the string
        for char in string:
            # If the character is an open parenthesis, increment the open count
            if char == '(':
                open_count += 1
            # If the character is a close parenthesis, increment the close count
            elif char == ')':
                close_count += 1

    # If the open and close counts are equal, the strings can be concatenated
    if open_count == close_count:
        return 'Yes'
    else:
        return 'No'

