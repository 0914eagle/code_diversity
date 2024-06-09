
from typing import List

def match_parens(lst: List[str]) -> str:
    
    # Initialize a counter to keep track of the number of open parentheses
    counter = 0
    # Iterate through the first string
    for char in lst[0]:
        # If the character is an open parentheses, increase the counter
        if char == '(':
            counter += 1
        # If the character is a close parentheses, decrease the counter
        elif char == ')':
            counter -= 1
        # If the counter goes below 0, return 'No'
        if counter < 0:
            return 'No'
    # Iterate through the second string
    for char in lst[1]:
        # If the character is an open parentheses, increase the counter
        if char == '(':
            counter += 1
        # If the character is a close parentheses, decrease the counter
        elif char == ')':
            counter -= 1
        # If the counter goes below 0, return 'No'
        if counter < 0:
            return 'No'
    # If the counter is not 0 at the end, return 'No'
    if counter != 0:
        return 'No'
    # Otherwise, return 'Yes'
    return 'Yes'

