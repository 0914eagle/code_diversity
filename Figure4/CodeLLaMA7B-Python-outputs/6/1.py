from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    return [max(nesting_level(paren_string, i) for i in range(len(paren_string))) for paren_string in paren_string.split()]


