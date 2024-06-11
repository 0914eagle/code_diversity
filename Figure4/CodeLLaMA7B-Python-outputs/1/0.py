from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    
    # initialize the list of results
    result = []
    # initialize the current string
    current_string = ''
    # initialize the current depth
    current_depth = 0
    # iterate through the string
    for char in paren_string:
        # if the character is an open brace
        if char == '(':
            # increment the depth
            current_depth += 1
        # if the character is a close brace
        elif char == ')':
            # decrement the depth
            current_depth -= 1
        # if the depth is 0
        if current_depth == 0:
            # add the current string to the list of results
            result.append(current_string)
            # reset the current string
            current_string = ''
        # otherwise
        else:
            # add the character to the current string
            current_string += char
    # return the list of results
    return result


if