from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    
    # initialize the stack
    stack = []
    # initialize the output list
    output = []
    # iterate through the string
    for char in paren_string:
        # if the character is an open brace, append it to the stack
        if char == "(":
            stack.append(char)
        # if the character is a close brace, pop the stack
        elif char == ")":
            stack.pop()
        # if the stack is empty and the character is a close brace, append the character to the output
        if len(stack) == 0 and char == ")":
            output.append(char)
    # return the output list
    return output


if