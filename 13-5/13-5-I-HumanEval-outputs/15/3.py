
from typing import List

def match_parens(lst: List[str]) -> str:
    
    # Initialize a counter for open parentheses
    count = 0
    # Iterate through the list of strings
    for s in lst:
        # If the current string is an open parenthesis, increase the counter
        if s == '(':
            count += 1
        # If the current string is a close parenthesis, decrease the counter
        elif s == ')':
            count -= 1
        # If the counter goes below 0, return 'No'
        if count < 0:
            return 'No'
    # If the counter is not 0 at the end, return 'No'
    if count != 0:
        return 'No'
    # Otherwise, return 'Yes'
    return 'Yes'

