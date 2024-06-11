from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    paren_stack = []
    paren_level = 0
    for char in paren_string:
        if char == '(':
            paren_stack.append(char)
            paren_level += 1
        elif char == ')':
            if paren_level == 0:
                return []
            paren_level -= 1
            paren_stack.pop()
        elif char == ' ' and paren_level == 0:
            return []
    return [paren_level] + parse_nested_parens(''.join(paren_stack))


