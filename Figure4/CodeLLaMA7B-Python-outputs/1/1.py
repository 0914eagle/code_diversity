from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    
    # initialize a stack to keep track of open parentheses
    stack = []
    # initialize a list to store the final result
    result = []
    # iterate through the string
    for char in paren_string:
        # if the character is an open brace, append it to the stack
        if char == '(':
            stack.append(char)
        # if the character is a close brace, pop the topmost element from the stack
        # and append it to the result list
        elif char == ')':
            result.append(stack.pop())
    # return the result list
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
