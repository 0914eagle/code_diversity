
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    levels = []
    current_level = 0
    for char in paren_string:
        if char == '(':
            current_level += 1
        elif char == ')':
            current_level -= 1
        if current_level > 0:
            levels.append(current_level)
    return levels

