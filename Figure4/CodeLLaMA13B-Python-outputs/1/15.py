from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    
    # HINT: you may want to use recursion for this
    # HINT: this problem can be solved in one line of Python if you are clever
    return [paren_string[i] for i in (paren_string.replace('(', ' ( ').replace(')', ' ) ').split()) if i != '']


if __name__ == '__main__':
    import doctest

    doctest.testmod()
