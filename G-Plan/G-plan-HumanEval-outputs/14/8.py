
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    def is_open_paren(c):
        return c == '('

    def is_close_paren(c):
        return c == ')'

    result = []
    stack = []
    start = 0

    for i, char in enumerate(paren_string):
        if is_open_paren(char):
            stack.append(i)
        elif is_close_paren(char):
            start = stack.pop()
            result.append(paren_string[start:i+1])

    return result

if __name__ == "__main__":
    paren_string = input().replace(" ", "")
    groups = separate_paren_groups(paren_string)
    print(groups)
