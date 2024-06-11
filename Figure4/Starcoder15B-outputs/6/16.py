from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    result = []
    for group in paren_string.split():
        result.append(max(parse_nested_parens_helper(group)))
    return result


