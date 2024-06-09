
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    level = 0
    max_level = 0
    levels = []
    for char in paren_string:
        if char == '(':
            level += 1
            if level > max_level:
                max_level = level
        elif char == ')':
            level -= 1
    levels.append(max_level)
    return levels

