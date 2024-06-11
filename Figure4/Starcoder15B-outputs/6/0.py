from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    return [max(map(len, re.findall(r'\(([^()]*)\)', paren_string))) for paren_string in paren_string.split()]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_challenge/level_01.py
#!/usr/bin/env python