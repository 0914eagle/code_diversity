from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    
    if not strings:
        return None
    if len(strings) == 1:
        return strings[0]
    if len(strings) == 2:
        return max(strings, key=len)
    return max(strings, key=len)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
