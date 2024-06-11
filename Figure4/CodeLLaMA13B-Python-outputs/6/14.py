from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    return [max(map(lambda x: x[1] - x[0] + 1, find_parens(paren_string, i))) for i in range(len(paren_string))]


