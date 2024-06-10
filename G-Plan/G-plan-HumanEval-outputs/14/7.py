
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    def is_open_paren(char):
        return char == '('

    def is_close_paren(char):
        return char == ')'

    result = []
    stack = []
    start = 0

    for i, char in enumerate(paren_string):
        if is_open_paren(char):
            stack.append(i)
        elif is_close_paren(char):
            open_index = stack.pop()
            group = paren_string[open_index:i+1]
            result.append(group)

    return result

if __name__ == "__main__":
    paren_string = input().replace(" ", "")
    groups = separate_paren_groups(paren_string)
    print(groups)
