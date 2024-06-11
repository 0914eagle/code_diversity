from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    
    # HINT: you may want to use recursion for this
    # HINT2: this problem can be solved in one line of Python code
    return [paren_string[i] for i in (paren_string.find('('), paren_string.rfind(')'))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
