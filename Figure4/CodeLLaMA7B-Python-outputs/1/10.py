from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    
    # initialize the stack
    stack = []
    # initialize the list of results
    results = []
    # iterate over the string
    for char in paren_string:
        # if the character is an open brace, append it to the stack
        if char == '(':
            stack.append(char)
        # if the character is a close brace
        elif char == ')':
            # pop the last open brace off the stack
            last_open_brace = stack.pop()
            # if the stack is empty, we have found a separate group
            if not stack:
                # add the result to the list of results
                results.append(last_open_brace + char)
    return results


if