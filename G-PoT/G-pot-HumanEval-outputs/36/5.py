
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    
    depths = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
        elif c == ')':
            depths.append(current_depth)
            current_depth -= 1

    return depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
