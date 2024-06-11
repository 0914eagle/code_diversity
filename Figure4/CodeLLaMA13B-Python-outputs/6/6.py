from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    return [max(map(lambda x: x[1] - x[0] + 1, find_all_parens(paren_string))) for paren_string in paren_string.split()]


