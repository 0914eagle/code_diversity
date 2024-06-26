
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    levels = []
    level = 0
    for char in paren_string:
        if char == '(':
            level += 1
        elif char == ')':
            level -= 1
        if level > max(levels):
            levels.append(level)
    return levels

