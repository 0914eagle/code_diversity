from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    return [max(0, len(x.strip("()")) - 1) for x in paren_string.split()]


if __name__ == "__main__":
    import doctest

    doctest.testmod