from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    return [max(map(len, re.findall(r'\(([^()]*?)\)', s))) for s in paren_string.split()]


if __name__ == '__