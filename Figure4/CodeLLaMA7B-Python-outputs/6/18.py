from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    # Your code here
    return [max(nesting(s)) for s in paren_string.split()]


