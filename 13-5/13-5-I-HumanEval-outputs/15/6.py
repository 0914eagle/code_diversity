
from typing import List

def match_parens(lst: List[str]) -> str:
    
    # Initialize a counter for open parentheses
    open_count = 0
    # Iterate through the list of strings
    for s in lst:
        # If the current string is '(', increase the open count by 1
        if s == '(':
            open_count += 1
        # If the current string is ')', decrease the open count by 1
        elif s == ')':
            open_count -= 1
        # If the open count becomes negative, return 'No'
        if open_count < 0:
            return 'No'
    # If the open count is not zero at the end, return 'No'
    if open_count != 0:
        return 'No'
    # Otherwise, return 'Yes'
    return 'Yes'

