from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    
    paren_groups = []
    paren_stack = []
    for char in paren_string:
        if char == '(':
            paren_stack.append(char)
        elif char == ')':
            if len(paren_stack) > 0:
                paren_stack.pop()
            else:
                paren_groups.append(''.join(paren_stack))
                paren_stack = []
    if len(paren_stack) > 0:
        paren_groups.append(''.join(paren_stack))
    return paren_groups


