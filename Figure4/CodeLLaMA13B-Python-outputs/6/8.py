from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    return [max(map(lambda x: 1 + x[1] - x[0], find_matching_parens(paren_string, i))) for i, _ in enumerate(paren_string.split())]


