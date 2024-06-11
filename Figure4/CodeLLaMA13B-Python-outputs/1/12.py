from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Hint: don't write any loops, you shouldn't need them
    return [paren_string[i] for i in range(len(paren_string)) if paren_string.count("(") == paren_string.count(")") and paren_string[i] != " "]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
