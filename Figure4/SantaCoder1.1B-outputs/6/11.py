from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    paren_stack = []
    for paren in paren_string.split():
        if paren == "(":
            paren_stack.append(paren)
        elif paren == ")":
            if len(paren_stack) == 0:
                raise ValueError("Invalid input")
            paren_stack.pop()
        else:
            raise ValueError("Invalid input")
    return paren_stack


