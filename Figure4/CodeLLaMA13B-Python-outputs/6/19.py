from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    

    return [max(map(lambda x: 1 + x[1] - x[0], re.findall(r'\([^(]*\)', paren_string))) for paren_string in paren_string.split()]


if