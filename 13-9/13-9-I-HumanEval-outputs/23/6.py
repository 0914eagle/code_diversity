
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    nested_levels = []
    for group in paren_string.split():
        nested_level = 0
        for char in group:
            if char == '(':
                nested_level += 1
            elif char == ')':
                nested_level -= 1
        nested_levels.append(nested_level)
    return nested_levels

