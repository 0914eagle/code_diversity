
from typing import List

def match_parens(lst: List[str]) -> str:
    
    # Initialize a counter to keep track of the number of open parentheses
    count = 0
    # Iterate through the list of strings
    for s in lst:
        # If the current string is an open parenthesis, increase the counter
        if s == "(":
            count += 1
        # If the current string is a close parenthesis, decrease the counter
        elif s == ")":
            count -= 1
        # If the counter goes below 0, it means that there are more close
        # parentheses than open parentheses, which is not balanced
        if count < 0:
            return "No"
    # If the counter is not 0 at the end, it means that there are more open
    # parentheses than close parentheses, which is not balanced
    if count != 0:
        return "No"
    # If the counter is 0, it means that all parentheses are balanced
    return "Yes"

