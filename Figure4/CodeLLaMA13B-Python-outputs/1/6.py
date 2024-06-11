from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    
    # HINT: you may want to use recursion for this
    # HINT: this problem can be solved in one line of Python
    return [paren_string[i] for i in (list(map(lambda x: x[0], filter(lambda x: x[1] == 0, enumerate(list(map(lambda x: 1 if x == '(' else -1, paren_string.replace(' ', ''))))))))]


