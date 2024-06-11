from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    paren_stack = []
    paren_level = 0
    for char in paren_string:
        if char == '(':
            paren_level += 1
        elif char == ')':
            paren_level -= 1
        if paren_level == 0:
            paren_stack.append(char)
        elif paren_level < 0:
            raise ValueError("Invalid string")
    return paren_stack


