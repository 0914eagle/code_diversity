from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    result = []
    for group in paren_string.split():
        result.append(max(group.count('('), group.count(')')))
    return result


if __name__ ==