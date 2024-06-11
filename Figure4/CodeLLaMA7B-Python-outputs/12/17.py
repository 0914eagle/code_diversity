from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    
    if not strings:
        return None

    longest_string = max(strings, key=len)
    return longest_string


if __name__ == "__main__":
    import doctest

    doctest.testmod