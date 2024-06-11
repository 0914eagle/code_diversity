from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    
    paren_stack = []
    paren_string = paren_string.strip()
    for char in paren_string:
        if char == '(':
            paren_stack.append('(')
        elif char == ')':
            if len(paren_stack) > 0 and paren_stack[-1] == '(':
                paren_stack.pop()
            else:
                paren_stack.append(')')
        elif char == ' ' and len(paren_stack) > 0 and paren_stack[-1] != '(':
            paren_stack.pop()
    return paren_stack


