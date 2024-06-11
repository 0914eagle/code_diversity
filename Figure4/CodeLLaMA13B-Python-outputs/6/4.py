from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    return [max(map(lambda x: x.count('(') - x.count(')'), paren_string.split())) for paren_string in paren_string.split()]


if __name__ == "__main__