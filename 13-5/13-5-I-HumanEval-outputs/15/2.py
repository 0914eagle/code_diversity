
from typing import List

def match_parens(lst: List[str]) -> str:
    
    # Initialize a counter to keep track of the number of open parentheses
    counter = 0
    # Iterate through the list of strings
    for s in lst:
        # Iterate through the characters in the string
        for c in s:
            # If the character is an open parenthesis, increase the counter
            if c == '(':
                counter += 1
            # If the character is a close parenthesis, decrease the counter
            elif c == ')':
                counter -= 1
        # If the counter goes below 0, it means there are more close parentheses than open parentheses
        if counter < 0:
            return 'No'
    # If the counter is not 0 at the end, it means there are more open parentheses than close parentheses
    if counter != 0:
        return 'No'
    # If the counter is 0, it means all parentheses are balanced
    return 'Yes'

