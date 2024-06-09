
from typing import List

def match_parens(lst: List[str]) -> str:
    
    # Initialize a counter to keep track of the number of open parentheses
    counter = 0
    # Iterate through the list of strings
    for s in lst:
        # If the current string is an open parentheses, increment the counter
        if s == '(':
            counter += 1
        # If the current string is a close parentheses, decrement the counter
        elif s == ')':
            counter -= 1
        # If the counter goes below 0, it means that there are more close
        # parentheses than open parentheses, which means that the string is not good
        if counter < 0:
            return 'No'
    # If the counter is not 0 at the end, it means that there are more open
    # parentheses than close parentheses, which means that the string is not good
    if counter != 0:
        return 'No'
    # If the string is good, return 'Yes'
    return 'Yes'

